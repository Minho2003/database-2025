from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.store import StoreCreate, StoreResponse
from app.schemas.owner import OwnerLogin
from app.services import owner as owner_service
from app.services import store as store_service
from typing import List

router = APIRouter(prefix="/stores", tags=["stores"])

@router.post("/register", response_model=StoreResponse)
def register_store(
    store: StoreCreate,
    owner_credentials: OwnerLogin,
    db: Session = Depends(get_db)
):
    # 사장 인증
    owner = owner_service.authenticate_owner(db, owner_credentials.owner_id, owner_credentials.owner_passwd)
    return store_service.create_store(db, store, owner.id)

@router.get("/category/{category_id}", response_model=List[StoreResponse])
def get_stores_by_category(category_id: int, db: Session = Depends(get_db)):
    return store_service.get_stores_by_category(db, category_id)

@router.get("/{store_id}", response_model=StoreResponse)
def get_store(store_id: int, db: Session = Depends(get_db)):
    return store_service.get_store(db, store_id)

@router.get("/owner/{owner_id}", response_model=List[StoreResponse])
def get_stores_by_owner(owner_id: str, db: Session = Depends(get_db)):
    owner = owner_service.get_owner(db, owner_id)
    return store_service.get_stores_by_owner(db, owner.id)

