from sqlalchemy.orm import Session
from app.models import Payment, Store
from app.schemas.payment import PaymentCreate
from fastapi import HTTPException

def add_payment_method(db: Session, store_id: int, payment: PaymentCreate):
    # 가게 존재 확인
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
    
    # 이미 등록된 결제 방식인지 확인
    existing = db.query(Payment).filter(
        Payment.store_id == store_id,
        Payment.payment == payment.payment
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="이미 등록된 결제 방식입니다")
    
    db_payment = Payment(
        store_id=store_id,
        payment=payment.payment
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def remove_payment_method(db: Session, store_id: int, payment_id: int):
    payment = db.query(Payment).filter(
        Payment.id == payment_id,
        Payment.store_id == store_id
    ).first()
    
    if not payment:
        raise HTTPException(status_code=404, detail="결제 방식을 찾을 수 없습니다")
    
    db.delete(payment)
    db.commit()
    return payment

def get_store_payments(db: Session, store_id: int):
    payments = db.query(Payment).filter(Payment.store_id == store_id).all()
    return payments

