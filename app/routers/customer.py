from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.category import CategoryResponse
from app.schemas.menu import MenuResponse
from app.schemas.payment import PaymentResponse
from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.store import StoreResponse
from app.schemas.coupon import CouponResponse
from app.schemas.user import UserLogin
from app.services import store_service
from app.services import store as store_service_store
from app.services import user as user_service
from app.services import coupon as coupon_service
from typing import List

router = APIRouter(prefix="/customer", tags=["customer"])

@router.get("/categories", response_model=List[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    return store_service.get_all_categories(db)

@router.get("/categories/{category_id}/stores", response_model=List[StoreResponse])
def get_stores_by_category(category_id: int, db: Session = Depends(get_db)):
    stores = store_service_store.get_stores_by_category(db, category_id)
    return stores

@router.get("/stores/{store_id}/menus", response_model=List[MenuResponse])
def get_store_menus(store_id: int, db: Session = Depends(get_db)):
    return store_service.get_menus_by_store(db, store_id)

@router.get("/stores/{store_id}/payments", response_model=List[PaymentResponse])
def get_store_payments(store_id: int, db: Session = Depends(get_db)):
    return store_service.get_payments_by_store(db, store_id)

@router.get("/stores/{store_id}/coupons", response_model=List[CouponResponse])
def get_store_coupons(store_id: int, db: Session = Depends(get_db)):
    return coupon_service.get_store_coupons(db, store_id)

@router.post("/orders", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    user_credentials: UserLogin,
    db: Session = Depends(get_db)):
    # 사용자 인증
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return store_service.create_order(db, user.id, order.store_id, order.order_details, order.total_price)

