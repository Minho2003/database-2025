import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Store(Base):
    __tablename__ = 'store'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    store_name = Column(String(50), nullable=False) # Varchar(50) -> String(50)
    category = Column(String(30), nullable=False) # category_id 외에 중복 저장 (스키마 따름)
    phone = Column(String(20), nullable=False)
    minprice = Column(String(30), nullable=False) # 스키마대로 String 타입 유지
    reviewCount = Column(Integer, nullable=False, default=0)
    operationTime = Column(String(250), nullable=False)
    closedDay = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=True, onupdate=func.now())
    
    owner = relationship('Owner', back_populates='stores')
    category_info = relationship('Category', back_populates='stores') 
    
    menus = relationship('Menu', back_populates='store')
    orders = relationship('Order', back_populates='store')
    favorites = relationship('Favorite_sotre', back_populates='store')
    payments = relationship('Payment', back_populates='store')
    coupons = relationship('Coupon', back_populates='store')
    reviews = relationship('Review', back_populates='store')
