from sqlalchemy.orm import Session
from app.models import Rider
from app.schemas.rider import RiderCreate
from fastapi import HTTPException

def create_rider(db: Session, rider: RiderCreate):
    # 중복 체크
    if db.query(Rider).filter(Rider.rider_id == rider.rider_id).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 라이더 ID입니다")
    
    db_rider = Rider(
        rider_id=rider.rider_id,
        phone=rider.phone,
        vehicle=rider.vehicle
    )
    db.add(db_rider)
    db.commit()
    db.refresh(db_rider)
    return db_rider

def get_rider(db: Session, rider_id: str):
    rider = db.query(Rider).filter(Rider.rider_id == rider_id).first()
    if not rider:
        raise HTTPException(status_code=404, detail="라이더를 찾을 수 없습니다")
    return rider

def get_all_riders(db: Session):
    riders = db.query(Rider).all()
    return riders
