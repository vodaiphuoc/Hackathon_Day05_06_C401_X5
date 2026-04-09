from fastapi import FastAPI, Depends, UploadFile, File, Body
from sqlmodel import Session, select, delete
from database import init_db, get_session
from models import ChatMessage, Property, ChatSession
from engine.rag_service import RAGService
import csv
from io import StringIO

app = FastAPI(title="VinHomes AI Sales Assistant")
rag = RAGService()

@app.on_event("startup")
def on_startup():
    init_db()

# ==========================================
# 1. API NẠP DỮ LIỆU TỪ FILE CSV
# ==========================================
@app.post("/upload")
async def upload_properties(file: UploadFile = File(...), db: Session = Depends(get_session)):
    content = await file.read()
    if not content:
        return {"status": "error", "message": "File CSV gửi lên bị rỗng!"}
        
    try:
        decoded_content = content.decode('utf-8-sig') 
        csv_reader = csv.DictReader(StringIO(decoded_content))
        
        texts, metadatas, ids = [], [], []
        count = 0
        
        for row in csv_reader:
            loai_hinh = row.get('LoaiHinh', 'Bất động sản')
            so_pn = row.get('SoPhongNgu', '')
            du_an = row.get('DuAn', 'Dự án')
            
            title = f"{loai_hinh} {so_pn}PN tại {du_an}".replace(" PN", "PN")
            price = f"{row.get('GiaTyVND', 'Thỏa thuận')} Tỷ"
            location = f"{row.get('PhuongXa', '')}, {row.get('QuanHuyen', '')}, {row.get('ThanhPho', '')}".strip(', ')
            
            description = (
                f"Mã tin: {row.get('MaTin')}. "
                f"Diện tích: {row.get('DienTich_m2')}m2, Tầng {row.get('Tang')}, ban công hướng {row.get('HuongBanCong')}. "
                f"Có {row.get('SoWC')} WC. Tình trạng: {row.get('TinhTrang')}. "
                f"Nội thất: {row.get('NoiThat')}. Pháp lý: {row.get('PhapLy')} (Bàn giao {row.get('NamBanGiao')}). "
                f"Phí quản lý: {row.get('PhiQuanLyNghin_m2')} nghìn/m2. "
                f"Tiện ích: {row.get('NoiBat')}, Đỗ xe: {row.get('ChoDoXe')}, Gym: {row.get('PhongGym')}, Hồ bơi: {row.get('HoBoi')}."
            )
            
            # Lưu Postgres lấy ID
            prop = Property(title=title, price=price, location=location, description=description)
            db.add(prop)
            db.commit()
            db.refresh(prop)
            
            # Chuẩn bị Data cho Qdrant
            full_text_for_ai = f"{title}. Vị trí: {location}. Giá: {price}. Chi tiết: {description}"
            texts.append(full_text_for_ai)
            metadatas.append(row) 
            ids.append(prop.id)
            count += 1
            
        # Nạp vào Vector DB
        rag.add_to_vdb(texts, metadatas, ids=ids)
            
        return {"status": "success", "message": f"Đã nạp {count} căn nhà từ file CSV vào hệ thống."}

    except Exception as e:
        db.rollback()
        return {"status": "error", "message": f"Lỗi xử lý file CSV: {str(e)}"}

@app.post("/chat")
async def chat(session_id: str = Body(...), message: str = Body(...), db: Session = Depends(get_session)):
    # Lấy 6 tin nhắn gần nhất làm Context
    statement = select(ChatMessage).where(ChatMessage.session_id == session_id).order_by(ChatMessage.created_at.desc()).limit(6)
    history = db.exec(statement).all()[::-1]
    
    # Gọi AI RAG Service
    answer = rag.generate_response(history, message)
    
    # Lưu tin nhắn vào Postgres
    db.add(ChatMessage(session_id=session_id, role="user", content=message))
    db.add(ChatMessage(session_id=session_id, role="assistant", content=answer))
    db.commit()
    
    return {"session_id": session_id, "answer": answer}

@app.delete("/delete_property/{property_id}")
async def delete_property(property_id: int, db: Session = Depends(get_session)):
    prop = db.get(Property, property_id)
    if not prop:
        return {"status": "error", "message": "Không tìm thấy căn nhà này."}
        
    db.delete(prop)
    db.commit()
    
    try:
        rag.delete_from_vdb([property_id])
    except Exception as e:
        print(f"Qdrant Delete Warning: {e}")
        
    return {"status": "success", "message": f"Đã xóa căn nhà ID {property_id}"}

@app.delete("/clear_all")
async def clear_all_data(db: Session = Depends(get_session)):
    # Dọn sạch Postgres
    db.exec(delete(Property))
    db.exec(delete(ChatMessage))
    db.commit()
    
    # Dọn sạch Qdrant
    rag.clear_all_vdb()
    
    return {"status": "success", "message": "Đã dọn sạch toàn bộ dữ liệu Postgres & Qdrant!"}

@app.get("/chat_history/{session_id}")
async def get_chat_history(session_id: str, db: Session = Depends(get_session)):
    # Lấy toàn bộ tin nhắn của session_id này, sắp xếp từ cũ đến mới (asc)
    statement = select(ChatMessage).where(ChatMessage.session_id == session_id).order_by(ChatMessage.created_at.asc())
    history = db.exec(statement).all()
    
    if not history:
        return {"session_id": session_id, "history": [], "message": "Chưa có lịch sử chat."}
        
    return {
        "session_id": session_id,
        "history": [{"role": msg.role, "content": msg.content, "time": msg.created_at} for msg in history]
    }

@app.post("/create_session")
async def create_session(db: Session = Depends(get_session)):
    new_session = ChatSession() # Tự động sinh UUID
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return {
        "status": "success", 
        "session_id": new_session.id, 
        "title": new_session.title
    }

@app.get("/sessions")
async def get_all_sessions(db: Session = Depends(get_session)):
    sessions = db.exec(select(ChatSession).order_by(desc(ChatSession.created_at))).all()
    return {"sessions": sessions}