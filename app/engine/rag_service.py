import os
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Qdrant
# Sửa lỗi import từ langchain.schema sang langchain_core.messages
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class RAGService:
    def __init__(self):
        # Đảm bảo host khớp với tên service trong docker-compose.yml (thường là 'qdrant')
        self.client = QdrantClient(host=os.getenv("QDRANT_HOST", "qdrant"), port=6333)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.collection_name = "vinhomes_knowledge"
        
        # Load System Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.txt")
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                self.system_instructions = f.read()
        except FileNotFoundError:
            self.system_instructions = "Bạn là trợ lý ảo VinHomes chuyên nghiệp."

    def add_to_vdb(self, texts, metadatas):
        Qdrant.from_texts(
            texts, self.embeddings, metadatas=metadatas,
            client=self.client, collection_name=self.collection_name
        )

    def generate_response(self, history, user_input):
        # Khởi tạo vectorstore để search
        vectorstore = Qdrant(
            client=self.client, 
            collection_name=self.collection_name, 
            embeddings=self.embeddings
        )
        
        # 1. Tìm kiếm context liên quan
        docs = vectorstore.similarity_search(user_input, k=3)
        context = "\n".join([d.page_content for d in docs])

        # 2. Xây dựng danh sách message gửi cho OpenAI
        messages = [SystemMessage(content=self.system_instructions)]
        
        # Thêm lịch sử chat từ Postgres
        for msg in history:
            if msg.role == "user":
                messages.append(HumanMessage(content=msg.content))
            else:
                messages.append(AIMessage(content=msg.content))

        # 3. Nạp Prompt cuối cùng kèm Context và câu hỏi hiện tại
        final_prompt = f"Thông tin tham khảo từ dự án:\n{context}\n\nCâu hỏi khách hàng: {user_input}"
        messages.append(HumanMessage(content=final_prompt))
        
        # Gọi LLM
        response = self.llm.invoke(messages)
        return response.content