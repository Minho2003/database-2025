from pydantic import BaseModel, EmailStr
from datetime import datetime

class OwnerCreate(BaseModel):
    owner_id: str
    owner_passwd: str
    email: EmailStr

class OwnerLogin(BaseModel):
    owner_id: str
    owner_passwd: str

class OwnerResponse(BaseModel):
    id: int
    owner_id: str
    email: str
    
    class Config:
        from_attributes = True

