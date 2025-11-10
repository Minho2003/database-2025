import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Review(Base):
    __tablename__ = 'review'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    content = Column(String(200), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=True, onupdate=func.now())
    
    user = relationship('User', back_populates='reviews')
    store = relationship('Store', back_populates='reviews')