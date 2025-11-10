from sqlalchemy.orm import Session
from app.models import Store, Menu
from app.schemas.store import StoreCreate
from fastapi import HTTPException

def create_store(db: Session, store: StoreCreate, owner_id: int):
    db_store = Store(
        owner_id=owner_id,
        category_id=store.category_id,
        store_name=store.store_name,
        category=store.category,
        phone=store.phone,
        minprice=store.minprice,
        operationTime=store.operationTime,
        closedDay=store.closedDay
    )
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    
    # 메뉴 등록
    if store.menus:
        for menu_item in store.menus:
            db_menu = Menu(
                store_id=db_store.id,
                menu=menu_item.menu,
                price=menu_item.price
            )
            db.add(db_menu)
        db.commit()
    
    return db_store

def get_stores_by_category(db: Session, category_id: int):
    stores = db.query(Store).filter(Store.category_id == category_id).all()
    return stores

def get_store(db: Session, store_id: int):
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
    return store

def get_stores_by_owner(db: Session, owner_id: int):
    stores = db.query(Store).filter(Store.owner_id == owner_id).all()
    return stores

