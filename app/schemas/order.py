from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    store_id: int
    order_details: str
    total_price: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    store_id: int
    rider_id: int
    order_details: str
    total_price: int
    order_time: datetime
    
    class Config:
        from_attributes = True

