from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewCreate(BaseModel):
    store_id: int
    rating: int
    content: Optional[str] = None

class ReviewResponse(BaseModel):
    id: int
    user_id: int
    store_id: int
    rating: int
    content: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

