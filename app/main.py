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

# @app.post("/upload")
# async def upload_properties(file: UploadFile = File(...), db: Session = Depends(get_session)):
#     content = await file.read()
#     data = json.loads(content) # Format: [{"title": "..", "description": "..", "price": ".."}]
    
#     texts = []
#     metadatas = []
    
#     for item in data:
#         # Lưu vào Postgres
#         prop = Property(**item)
#         db.add(prop)
#         # Chuẩn bị cho Qdrant
#         texts.append(f"{item['title']}: {item['description']}")
#         metadatas.append(item)
    
#     db.commit()
#     rag.add_to_vdb(texts, metadatas)
#     return {"message": f"Đã nạp {len(data)} bất động sản vào hệ thống."}

@app.post("/upload")
async def upload_properties(file: UploadFile = File(...), db: Session = Depends(get_session)):
    content = await file.read()
    
    # BẢO VỆ 1: Chống file rỗng
    if not content:
        return {"status": "error", "message": "File JSON gửi lên bị rỗng!"}
        
    try:
        data = json.loads(content)
        texts = []
        metadatas = []
        
        for item in data:
            # BẢO VỆ 2: Chống lỗi thiếu trường 'location' trong JSON
            if "location" not in item:
                item["location"] = "Đang cập nhật" # Gán mặc định nếu JSON thiếu
                
            # Lưu vào Postgres
            prop = Property(**item)
            db.add(prop)
            
            # Chuẩn bị cho Qdrant
            texts.append(f"{item['title']} tại {item['location']}: {item['description']}")
            metadatas.append(item)
        
        db.commit()
        
        # BẢO VỆ 3: Chống lỗi sập AI khi upload
        try:
            rag.add_to_vdb(texts, metadatas)
        except Exception as e:
            db.rollback() # Xóa DB nếu Qdrant lỗi
            return {"status": "error", "message": f"Lỗi nạp vector Qdrant: {str(e)}"}
            
        return {"status": "success", "message": f"Đã nạp {len(data)} bất động sản vào hệ thống."}

    except json.JSONDecodeError as e:
        return {"status": "error", "message": f"File JSON sai định dạng: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi hệ thống: {str(e)}"}
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