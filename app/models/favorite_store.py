import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Favorite_sotre(Base):
    __tablename__ = 'favorite_sotre'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False) 
    
    user = relationship('User', back_populates='favorites')
    store = relationship('Store', back_populates='favorites')