from pydantic import BaseModel
from datetime import datetime

class MenuResponse(BaseModel):
    id: int
    store_id: int
    menu: str
    price: int
    created_at: datetime
    
    class Config:
        from_attributes = True

