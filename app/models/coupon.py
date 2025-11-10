import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Coupon(Base):
    __tablename__ = 'coupon'
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    period = Column(Integer, nullable=True)
    discount = Column(Integer, nullable=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    
    store = relationship('Store', back_populates='coupons')
