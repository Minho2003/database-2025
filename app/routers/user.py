from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services import user as user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserLogin)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.post("/login", response_model=UserResponse)
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, credentials.user_id, credentials.passwd)
    return user

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)

@router.post("/modify/address", response_model=UserResponse)
def modify_user_address(user_credentials: UserLogin, address: str, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return user_service.modify_user_address(db, user.id, address)