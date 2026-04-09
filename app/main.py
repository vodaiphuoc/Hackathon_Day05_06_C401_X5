from fastapi import FastAPI, Depends, UploadFile, File
from sqlmodel import Session, select
from database import engine, init_db, get_session
from models import ChatMessage, Property
from engine.rag_service import RAGService
import json

app = FastAPI()
rag = RAGService()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/upload")
async def upload_properties(file: UploadFile = File(...), db: Session = Depends(get_session)):
    content = await file.read()
    data = json.loads(content) # Format: [{"title": "..", "description": "..", "price": ".."}]
    
    for item in data:
        # Lưu vào Postgres
        prop = Property(**item)
        db.add(prop)
        # Chuẩn bị và nạp vào Qdrant
        text = f"{item['title']}: {item['description']}"
        rag.add_to_vdb(text, item)
    
    db.commit()
    return {"message": f"Đã nạp {len(data)} bất động sản vào hệ thống."}

@app.post("/persist_state")
async def persist_state(session_id: str, message: str, db: Session = Depends(get_session)):
    # 1. Lấy lịch sử 5 tin nhắn gần nhất từ Postgres
    statement = select(ChatMessage).where(ChatMessage.session_id == session_id).order_by(ChatMessage.created_at.desc()).limit(5)
    history = db.exec(statement).all()[::-1]

    # 2. Gọi AI xử lý RAG
    ai_answer = rag.generate_response(history, message)

    # 3. Lưu cả User message và AI response vào Postgres
    db.add(ChatMessage(session_id=session_id, role="user", content=message))
    db.add(ChatMessage(session_id=session_id, role="assistant", content=ai_answer))
    db.commit()

    return {"answer": ai_answer}