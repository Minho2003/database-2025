from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CouponCreate(BaseModel):
    discount: int
    period: Optional[int] = None  # 사용 가능 기간 (일 단위)

class CouponResponse(BaseModel):
    id: int
    store_id: int
    discount: int
    period: Optional[int]
    is_deleted: bool
    
    class Config:
        from_attributes = True

