from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Chat(BaseModel):
    title: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    messages: List[Message] = []

class ChatResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    messages: List[Message] = []

class ChatListItem(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime

class MessageRequest(BaseModel):
    content: str

class MessageResponse(BaseModel):
    role: str
    content: str
    timestamp: datetime
