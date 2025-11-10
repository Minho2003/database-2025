from sqlalchemy.orm import Session
from app.models import Favorite_sotre, Store
from app.schemas.favorite_store import FavoriteStoreCreate
from fastapi import HTTPException

def add_favorite(db: Session, user_id: int, favorite: FavoriteStoreCreate):
    # 이미 찜한 가게인지 확인
    existing = db.query(Favorite_sotre).filter(
        Favorite_sotre.user_id == user_id,
        Favorite_sotre.store_id == favorite.store_id,
        Favorite_sotre.is_deleted == False
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="이미 찜한 가게입니다")
    
    # 가게 존재 확인
    store = db.query(Store).filter(Store.id == favorite.store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
    
    # 기존에 삭제된 찜이 있으면 복구
    deleted_favorite = db.query(Favorite_sotre).filter(
        Favorite_sotre.user_id == user_id,
        Favorite_sotre.store_id == favorite.store_id,
        Favorite_sotre.is_deleted == True
    ).first()
    
    if deleted_favorite:
        deleted_favorite.is_deleted = False
        db.commit()
        db.refresh(deleted_favorite)
        return deleted_favorite
    
    # 새로 찜하기
    db_favorite = Favorite_sotre(
        user_id=user_id,
        store_id=favorite.store_id
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def remove_favorite(db: Session, user_id: int, store_id: int):
    favorite = db.query(Favorite_sotre).filter(
        Favorite_sotre.user_id == user_id,
        Favorite_sotre.store_id == store_id,
        Favorite_sotre.is_deleted == False
    ).first()
    
    if not favorite:
        raise HTTPException(status_code=404, detail="찜한 가게를 찾을 수 없습니다")
    
    favorite.is_deleted = True
    db.commit()
    return favorite

def get_favorite_stores(db: Session, user_id: int):
    favorites = db.query(Favorite_sotre).filter(
        Favorite_sotre.user_id == user_id,
        Favorite_sotre.is_deleted == False
    ).all()
    
    # 가게 정보와 함께 반환
    stores = []
    for fav in favorites:
        store = db.query(Store).filter(Store.id == fav.store_id).first()
        if store:
            stores.append(store)
    
    return stores

