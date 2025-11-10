from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.owner import OwnerCreate, OwnerLogin, OwnerResponse
from app.services import owner as owner_service

router = APIRouter(prefix="/owners", tags=["owners"])

@router.post("/register", response_model=OwnerResponse)
def register_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    return owner_service.create_owner(db, owner)

@router.post("/login", response_model=OwnerResponse)
def login_owner(credentials: OwnerLogin, db: Session = Depends(get_db)):
    owner = owner_service.authenticate_owner(db, credentials.owner_id, credentials.owner_passwd)
    return owner

@router.get("/{owner_id}", response_model=OwnerResponse)
def get_owner(owner_id: str, db: Session = Depends(get_db)):
    return owner_service.get_owner(db, owner_id)

