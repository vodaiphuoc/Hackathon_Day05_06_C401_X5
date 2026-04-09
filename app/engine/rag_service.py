import os
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Qdrant
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class RAGService:
    def __init__(self):
        self.client = QdrantClient(host=os.getenv("QDRANT_HOST", "qdrant"), port=6333)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.collection_name = "vinhomes_knowledge"
        
        # 1. Tự động tạo Collection nếu Qdrant hoàn toàn trống
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
            )

        # 2. Khởi tạo VectorStore đúng chuẩn (Chỉ làm 1 lần)
        self.vectorstore = Qdrant(
            client=self.client, 
            collection_name=self.collection_name, 
            embeddings=self.embeddings
        )
        
        # Load System Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.txt")
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                self.system_instructions = f.read()
        except FileNotFoundError:
            self.system_instructions = "Bạn là trợ lý ảo VinHomes chuyên nghiệp."

    def add_to_vdb(self, texts, metadatas, ids=None):
        # Truyền thêm tham số ids vào. 
        # Qdrant sẽ tự hiểu: ID mới -> Thêm, ID cũ -> Cập nhật đè lên.
        self.vectorstore.add_texts(texts=texts, metadatas=metadatas, ids=ids)

    def delete_from_vdb(self, ids):
        # Hàm xóa data theo ID
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=ids
        )

    def clear_all_vdb(self):
        # Hàm reset toàn bộ (Rất hữu ích khi test Hackathon)
        # Xóa collection cũ và tạo lại cái mới tinh
        self.client.delete_collection(self.collection_name)
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )
        # Khởi tạo lại vectorstore
        self.vectorstore = Qdrant(
            client=self.client, 
            collection_name=self.collection_name, 
            embeddings=self.embeddings
        )

    def generate_response(self, history, user_input):
        try:
            # BƯỚC 1: Tự lấy model OpenAI dịch câu hỏi thành Vector (dãy số)
            query_vector = self.embeddings.embed_query(user_input)
            
            # BƯỚC 2: Bỏ qua LangChain, chọc thẳng vào Qdrant gốc
            # Kiểm tra xem Qdrant đang dùng hàm đời mới hay đời cũ để gọi cho chuẩn
            if hasattr(self.client, 'query_points'):
                results = self.client.query_points(
                    collection_name=self.collection_name,
                    query=query_vector,
                    limit=3
                ).points
            else:
                results = self.client.search(
                    collection_name=self.collection_name,
                    query_vector=query_vector,
                    limit=3
                )
            
            # BƯỚC 3: Móc ruột dữ liệu (LangChain giấu text ở cái key tên là 'page_content' trong Payload)
            context = "\n".join([point.payload.get("page_content", "") for point in results if point.payload])
            
        except Exception as e:
            print(f"🛑 Lỗi Hack Qdrant Search: {e}")
            context = ""

        # --- PHẦN GỌI AI GIỮ NGUYÊN ---
        messages = [SystemMessage(content=self.system_instructions)]
        
        for msg in history:
            if msg.role == "user":
                messages.append(HumanMessage(content=msg.content))
            else:
                messages.append(AIMessage(content=msg.content))

        if context.strip():
            final_prompt = (
                f"Dưới đây là thông tin các căn nhà phù hợp nhất:\n{context}\n\n"
                f"Dựa vào thông tin trên, hãy trả lời khách hàng: {user_input}"
            )
        else:
            final_prompt = f"Câu hỏi khách hàng: {user_input}"
            
        messages.append(HumanMessage(content=final_prompt))
        
        response = self.llm.invoke(messages)
        return response.content