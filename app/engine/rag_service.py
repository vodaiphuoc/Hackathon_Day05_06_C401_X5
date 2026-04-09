# import os
# from qdrant_client import QdrantClient
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_community.vectorstores import Qdrant
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# class RAGService:
#     def __init__(self):
#         # Đảm bảo host khớp với tên service trong docker-compose.yml (thường là 'qdrant')
#         self.client = QdrantClient(host=os.getenv("QDRANT_HOST", "qdrant"), port=6333)
#         self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
#         self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
#         self.collection_name = "vinhomes_knowledge"
        
#         # Load System Prompt
#         prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.txt")
#         try:
#             with open(prompt_path, "r", encoding="utf-8") as f:
#                 self.system_instructions = f.read()
#         except FileNotFoundError:
#             self.system_instructions = "Bạn là trợ lý ảo VinHomes chuyên nghiệp."

#     def add_to_vdb(self, texts, metadatas):
#         Qdrant.from_texts(
#             texts, self.embeddings, metadatas=metadatas,
#             client=self.client, collection_name=self.collection_name
#         )

#     def generate_response(self, history, user_input):
#         # Khởi tạo vectorstore để search
#         vectorstore = Qdrant(
#             client=self.client, 
#             collection_name=self.collection_name, 
#             embeddings=self.embeddings
#         )
        
#         # 1. Tìm kiếm context liên quan
#         docs = vectorstore.similarity_search(user_input, k=3)
#         context = "\n".join([d.page_content for d in docs])

#         # 2. Xây dựng danh sách message gửi cho OpenAI
#         messages = [SystemMessage(content=self.system_instructions)]
        
#         # Thêm lịch sử chat từ Postgres
#         for msg in history:
#             if msg.role == "user":
#                 messages.append(HumanMessage(content=msg.content))
#             else:
#                 messages.append(AIMessage(content=msg.content))

#         # 3. Nạp Prompt cuối cùng kèm Context và câu hỏi hiện tại
#         final_prompt = f"Thông tin tham khảo từ dự án:\n{context}\n\nCâu hỏi khách hàng: {user_input}"
#         messages.append(HumanMessage(content=final_prompt))
        
#         # Gọi LLM
#         response = self.llm.invoke(messages)
#         return response.content

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
            docs = self.vectorstore.similarity_search(user_input, k=3)
            context = "\n".join([d.page_content for d in docs])
        except Exception as e:
            print(f"Lỗi Vector Search: {e}")
            context = ""

        messages = [SystemMessage(content=self.system_instructions)]
        
        for msg in history:
            if msg.role == "user":
                messages.append(HumanMessage(content=msg.content))
            else:
                messages.append(AIMessage(content=msg.content))

        if context.strip():
            final_prompt = f"Thông tin tham khảo từ dự án:\n{context}\n\nCâu hỏi khách hàng: {user_input}"
        else:
            final_prompt = f"Câu hỏi khách hàng: {user_input}"
            
        messages.append(HumanMessage(content=final_prompt))
        
        response = self.llm.invoke(messages)
        return response.content