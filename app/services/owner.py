from sqlalchemy.orm import Session
from app.models import Owner
from app.schemas.owner import OwnerCreate
from fastapi import HTTPException

def create_owner(db: Session, owner: OwnerCreate):
    # 중복 체크
    if db.query(Owner).filter(Owner.owner_id == owner.owner_id).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 사장 ID입니다")
    if db.query(Owner).filter(Owner.email == owner.email).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다")
    
    db_owner = Owner(
        owner_id=owner.owner_id,
        owner_passwd=owner.owner_passwd,
        email=owner.email
    )
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def authenticate_owner(db: Session, owner_id: str, owner_passwd: str):
    owner = db.query(Owner).filter(Owner.owner_id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=401, detail="사장 ID 또는 비밀번호가 잘못되었습니다")
    if owner.owner_passwd != owner_passwd:
        raise HTTPException(status_code=401, detail="사장 ID 또는 비밀번호가 잘못되었습니다")
    return owner

def get_owner(db: Session, owner_id: str):
    owner = db.query(Owner).filter(Owner.owner_id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="사장을 찾을 수 없습니다")
    return owner
