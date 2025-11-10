from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.coupon import CouponCreate, CouponResponse
from app.schemas.owner import OwnerLogin
from app.services import coupon as coupon_service
from app.services import owner as owner_service
from app.services import store as store_service
from typing import List

router = APIRouter(prefix="/coupons", tags=["coupons"])

@router.post("/store/{store_id}", response_model=CouponResponse)
def create_coupon(
    store_id: int,
    coupon: CouponCreate,
    owner_credentials: OwnerLogin,
    db: Session = Depends(get_db)
):
    # 사장 인증
    owner = owner_service.authenticate_owner(db, owner_credentials.owner_id, owner_credentials.owner_passwd)
    
    # 가게 소유권 확인
    store = store_service.get_store(db, store_id)
    if store.owner_id != owner.id:
        raise HTTPException(status_code=403, detail="해당 가게의 소유자가 아닙니다")
    
    return coupon_service.create_coupon(db, store_id, coupon)

@router.get("/store/{store_id}", response_model=List[CouponResponse])
def get_store_coupons(store_id: int, db: Session = Depends(get_db)):
    return coupon_service.get_store_coupons(db, store_id)

@router.delete("/store/{store_id}/{coupon_id}")
def delete_coupon(
    store_id: int,
    coupon_id: int,
    owner_credentials: OwnerLogin,
    db: Session = Depends(get_db)
):
    # 사장 인증
    owner = owner_service.authenticate_owner(db, owner_credentials.owner_id, owner_credentials.owner_passwd)
    
    # 가게 소유권 확인
    store = store_service.get_store(db, store_id)
    if store.owner_id != owner.id:
        raise HTTPException(status_code=403, detail="해당 가게의 소유자가 아닙니다")
    
    return coupon_service.delete_coupon(db, store_id, coupon_id)

