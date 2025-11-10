from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.database import get_db
from app.schemas.review import ReviewCreate, ReviewResponse
from app.schemas.user import UserLogin
from app.services import review as review_service
from app.services import user as user_service
from typing import List

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("", response_model=ReviewResponse)
def create_review(
    review: ReviewCreate,
    user_credentials: UserLogin,
    db: Session = Depends(get_db)
):
    # 사용자 인증
    user = user_service.authenticate_user(db, user_credentials.user_id, user_credentials.passwd)
    return review_service.create_review(db, user.id, review)

@router.get("/store/{store_id}", response_model=List[ReviewResponse])
def get_store_reviews(store_id: int, db: Session = Depends(get_db)):
    return review_service.get_store_reviews(db, store_id)

