import uuid

from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class ChatMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str = Field(index=True)
    role: str # 'user' hoặc 'assistant'
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Property(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    price: str
    location: str
    description: str

class ChatSession(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str = Field(default="Tư vấn mua nhà mới")
    created_at: datetime = Field(default_factory=datetime.utcnow)