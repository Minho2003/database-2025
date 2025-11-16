from flask import Blueprint, request, jsonify
from models import db, Coupon, Store
from utils.auth import owner_required, get_current_owner, verify_store_ownership

bp = Blueprint('coupons', __name__)

@bp.route('/store/<int:store_id>', methods=['POST'])
@owner_required
def create_coupon(store_id):
    """쿠폰 생성 (사장 인증 + 소유권 확인)"""
    owner = get_current_owner()
    if not owner:
        return jsonify({'error': '사장 인증이 필요합니다.'}), 401
    
    # 가게 소유권 확인
    if not verify_store_ownership(store_id, owner.id):
        return jsonify({'error': '가게 소유권이 없습니다.'}), 403
    
    data = request.get_json()
    
    coupon = Coupon(
        store_id=store_id,
        period=data.get('period'),
        discount=data.get('discount'),
        is_deleted=False
    )
    
    try:
        db.session.add(coupon)
        db.session.commit()
        return jsonify({'message': '쿠폰이 생성되었습니다.', 'coupon_id': coupon.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/store/<int:store_id>', methods=['GET'])
def get_store_coupons(store_id):
    """가게 쿠폰 목록"""
    coupons = Coupon.query.filter_by(store_id=store_id, is_deleted=False).all()
    return jsonify([{
        'id': coupon.id,
        'period': coupon.period,
        'discount': coupon.discount
    } for coupon in coupons]), 200

@bp.route('/store/<int:store_id>/<int:coupon_id>', methods=['DELETE'])
@owner_required
def delete_coupon(store_id, coupon_id):
    """쿠폰 삭제 (사장 인증 + 소유권 확인)"""
    owner = get_current_owner()
    if not owner:
        return jsonify({'error': '사장 인증이 필요합니다.'}), 401
    
    # 가게 소유권 확인
    if not verify_store_ownership(store_id, owner.id):
        return jsonify({'error': '가게 소유권이 없습니다.'}), 403
    
    coupon = Coupon.query.filter_by(id=coupon_id, store_id=store_id).first()
    if not coupon:
        return jsonify({'error': '쿠폰을 찾을 수 없습니다.'}), 404
    
    coupon.is_deleted = True
    
    try:
        db.session.commit()
        return jsonify({'message': '쿠폰이 삭제되었습니다.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

