from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.schemas.owner import OwnerLogin
from app.services import payment as payment_service
from app.services import owner as owner_service
from app.services import store as store_service
from typing import List

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/store/{store_id}", response_model=PaymentResponse)
def add_payment_method(
    store_id: int,
    payment: PaymentCreate,
    owner_credentials: OwnerLogin,
    db: Session = Depends(get_db)
):
    # 사장 인증
    owner = owner_service.authenticate_owner(db, owner_credentials.owner_id, owner_credentials.owner_passwd)
    
    # 가게 소유권 확인
    store = store_service.get_store(db, store_id)
    if store.owner_id != owner.id:
        raise HTTPException(status_code=403, detail="해당 가게의 소유자가 아닙니다")
    
    return payment_service.add_payment_method(db, store_id, payment)

@router.delete("/store/{store_id}/{payment_id}")
def remove_payment_method(
    store_id: int,
    payment_id: int,
    owner_credentials: OwnerLogin,
    db: Session = Depends(get_db)
):
    # 사장 인증
    owner = owner_service.authenticate_owner(db, owner_credentials.owner_id, owner_credentials.owner_passwd)
    
    # 가게 소유권 확인
    store = store_service.get_store(db, store_id)
    if store.owner_id != owner.id:
        raise HTTPException(status_code=403, detail="해당 가게의 소유자가 아닙니다")
    
    return payment_service.remove_payment_method(db, store_id, payment_id)

@router.get("/store/{store_id}", response_model=List[PaymentResponse])
def get_store_payments(store_id: int, db: Session = Depends(get_db)):
    return payment_service.get_store_payments(db, store_id)

