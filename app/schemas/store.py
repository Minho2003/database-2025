from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class MenuItem(BaseModel):
    menu: str
    price: int

class StoreCreate(BaseModel):
    category_id: int
    store_name: str
    category: str
    phone: str
    minprice: str
    operationTime: str
    closedDay: str
    menus: Optional[List[MenuItem]] = []

class StoreResponse(BaseModel):
    id: int
    owner_id: int
    category_id: int
    store_name: str
    category: str
    phone: str
    minprice: str
    reviewCount: int
    operationTime: str
    closedDay: str
    created_at: datetime
    
    class Config:
        from_attributes = True

