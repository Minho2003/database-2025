from flask import Blueprint, request, jsonify
from models import db, Review, Store
from utils.auth import login_required, get_current_user

bp = Blueprint('reviews', __name__)

@bp.route('', methods=['POST'])
@login_required
def create_review():
    """리뷰 작성 (사용자 인증 필요)"""
    user = get_current_user()
    if not user:
        return jsonify({'error': '사용자를 찾을 수 없습니다.'}), 404
    
    data = request.get_json()
    
    if not all(k in data for k in ['store_id', 'rating']):
        return jsonify({'error': '가게 ID와 평점이 필요합니다.'}), 400
    
    store_id = data['store_id']
    
    # 가게 존재 확인
    store = Store.query.get(store_id)
    if not store:
        return jsonify({'error': '존재하지 않는 가게입니다.'}), 404
    
    # 평점 유효성 검사
    rating = data['rating']
    if not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({'error': '평점은 1~5 사이의 정수여야 합니다.'}), 400
    
    review = Review(
        user_id=user.id,
        store_id=store_id,
        rating=rating,
        content=data.get('content', '')
    )
    
    try:
        db.session.add(review)
        # 가게의 리뷰 개수 업데이트
        store.reviewCount = Review.query.filter_by(store_id=store_id).count() + 1
        db.session.commit()
        return jsonify({'message': '리뷰가 작성되었습니다.', 'review_id': review.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/store/<int:store_id>', methods=['GET'])
def get_store_reviews(store_id):
    """가게 리뷰 목록"""
    reviews = Review.query.filter_by(store_id=store_id).order_by(Review.created_at.desc()).all()
    return jsonify([{
        'id': review.id,
        'user_id': review.user_id,
        'user_name': review.user.name if review.user else None,
        'rating': review.rating,
        'content': review.content,
        'created_at': review.created_at.isoformat()
    } for review in reviews]), 200

