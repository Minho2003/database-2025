from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    user_id: str
    passwd: str
    email: EmailStr
    name: str
    address: str

class UserLogin(BaseModel):
    user_id: str
    passwd: str

class UserResponse(BaseModel):
    id: int
    user_id: str
    email: str
    name: str
    address: str
    created_at: datetime
    
    class Config:
        from_attributes = True

