import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(30), nullable=False, unique=True)
    passwd = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now()) 

    reviews = relationship('Review', back_populates='user')
    orders = relationship('Order', back_populates='user')
    favorites = relationship('Favorite_sotre', back_populates='user') 