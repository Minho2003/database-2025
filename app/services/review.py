from sqlalchemy.orm import Session
from app.models import Review, Store, Order
from app.schemas.review import ReviewCreate
from fastapi import HTTPException

def create_review(db: Session, user_id: int, review: ReviewCreate):
    # 가게 존재 확인
    store = db.query(Store).filter(Store.id == review.store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
    
    # 해당 가게에서 주문한 이력이 있는지 확인 (선택사항 - 요구사항에 따라)
    # order = db.query(Order).filter(
    #     Order.user_id == user_id,
    #     Order.store_id == review.store_id
    # ).first()
    # if not order:
    #     raise HTTPException(status_code=400, detail="해당 가게에서 주문한 이력이 없습니다")
    
    # 이미 리뷰를 작성했는지 확인 (선택사항)
    existing_review = db.query(Review).filter(
        Review.user_id == user_id,
        Review.store_id == review.store_id
    ).first()
    
    if existing_review:
        raise HTTPException(status_code=400, detail="이미 리뷰를 작성하셨습니다")
    
    # 리뷰 생성
    db_review = Review(
        user_id=user_id,
        store_id=review.store_id,
        rating=review.rating,
        content=review.content
    )
    db.add(db_review)
    
    # 가게의 리뷰 개수 업데이트
    store.reviewCount = db.query(Review).filter(Review.store_id == review.store_id).count() + 1
    db.commit()
    db.refresh(db_review)
    return db_review

def get_store_reviews(db: Session, store_id: int):
    reviews = db.query(Review).filter(Review.store_id == store_id).all()
    return reviews

