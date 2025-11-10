from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.favorite_store import FavoriteStoreCreate, FavoriteStoreResponse
from app.schemas.store import StoreResponse
from app.schemas.user import UserLogin
from app.services import favorite_store as favorite_service
from app.services import user as user_service
from typing import List

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("", response_model=FavoriteStoreResponse)
def add_favorite(
    favorite: FavoriteStoreCreate,
    user_credentials: UserLogin,
    db: Session = Depends(get_db)
):
    # 사용자 인증
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return favorite_service.add_favorite(db, user.id, favorite)

@router.delete("/{store_id}")
def remove_favorite(
    store_id: int,
    user_credentials: UserLogin,
    db: Session = Depends(get_db)
):
    # 사용자 인증
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return favorite_service.remove_favorite(db, user.id, store_id)

@router.get("", response_model=List[StoreResponse])
def get_favorite_stores(
    user_credentials: UserLogin,
    db: Session = Depends(get_db)
):
    # 사용자 인증
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return favorite_service.get_favorite_stores(db, user.id)

