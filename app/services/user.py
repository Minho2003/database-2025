from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate):
    # 중복 체크
    if db.query(User).filter(User.user_id == user.user_id).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자 ID입니다")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다")
    
    db_user = User(
        user_id=user.user_id,
        passwd=user.passwd,
        email=user.email,
        name=user.name,
        address=user.address
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user_id: str, passwd: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="사용자 ID 또는 비밀번호가 잘못되었습니다")
    if user.passwd != passwd:
        raise HTTPException(status_code=401, detail="사용자 ID 또는 비밀번호가 잘못되었습니다")
    return user

def get_user(db: Session, user_id: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    return user

def modify_user_address(db: Session, user_id: str, address: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    user.address = address
    db.commit()
    db.refresh(user)
    return user


