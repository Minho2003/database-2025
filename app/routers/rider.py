from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.rider import RiderCreate, RiderResponse
from app.services import rider as rider_service

router = APIRouter(prefix="/riders", tags=["riders"])

@router.post("/register", response_model=RiderResponse)
def register_rider(rider: RiderCreate, db: Session = Depends(get_db)):
    return rider_service.create_rider(db, rider)

@router.get("/{rider_id}", response_model=RiderResponse)
def get_rider(rider_id: str, db: Session = Depends(get_db)):
    return rider_service.get_rider(db, rider_id)

