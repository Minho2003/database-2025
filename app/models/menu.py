import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Menu(Base):
    __tablename__ = 'menu'
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    menu = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=True, onupdate=func.now()) 
    
    # Relationship
    store = relationship('Store', back_populates='menus')