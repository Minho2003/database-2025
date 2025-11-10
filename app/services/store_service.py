from sqlalchemy.orm import Session
from app.models import Category, Menu, Payment, Order, Rider
from fastapi import HTTPException
import random

def get_all_categories(db: Session):
    categories = db.query(Category).all()
    return categories

def get_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="카테고리를 찾을 수 없습니다")
    return category

def get_menus_by_store(db: Session, store_id: int):
    menus = db.query(Menu).filter(Menu.store_id == store_id).all()
    return menus

def get_payments_by_store(db: Session, store_id: int):
    payments = db.query(Payment).filter(Payment.store_id == store_id).all()
    return payments

def create_order(db: Session, user_id: int, store_id: int, order_details: str, total_price: int):
    # 랜덤으로 라이더 할당
    riders = db.query(Rider).all()
    if not riders:
        raise HTTPException(status_code=400, detail="배정 가능한 라이더가 없습니다")
    rider = random.choice(riders)
    
    db_order = Order(
        user_id=user_id,
        store_id=store_id,
        rider_id=rider.id,
        order_details=order_details,
        total_price=total_price
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

