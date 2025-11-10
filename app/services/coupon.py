from sqlalchemy.orm import Session
from app.models import Coupon, Store
from app.schemas.coupon import CouponCreate
from fastapi import HTTPException
from datetime import datetime, timedelta

def create_coupon(db: Session, store_id: int, coupon: CouponCreate):
    # 가게 존재 확인
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
    
    db_coupon = Coupon(
        store_id=store_id,
        discount=coupon.discount,
        period=coupon.period
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

def get_store_coupons(db: Session, store_id: int):
    coupons = db.query(Coupon).filter(
        Coupon.store_id == store_id,
        Coupon.is_deleted == False
    ).all()
    return coupons

def delete_coupon(db: Session, store_id: int, coupon_id: int):
    coupon = db.query(Coupon).filter(
        Coupon.id == coupon_id,
        Coupon.store_id == store_id,
        Coupon.is_deleted == False
    ).first()
    
    if not coupon:
        raise HTTPException(status_code=404, detail="쿠폰을 찾을 수 없습니다")
    
    coupon.is_deleted = True
    db.commit()
    return coupon

