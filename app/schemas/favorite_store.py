from pydantic import BaseModel
from datetime import datetime

class FavoriteStoreCreate(BaseModel):
    store_id: int

class FavoriteStoreResponse(BaseModel):
    id: int
    user_id: int
    store_id: int
    created_at: datetime
    is_deleted: bool
    
    class Config:
        from_attributes = True

