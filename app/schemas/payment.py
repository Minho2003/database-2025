from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentCreate(BaseModel):
    payment: str

class PaymentResponse(BaseModel):
    id: int
    store_id: int
    payment: str
    
    class Config:
        from_attributes = True
