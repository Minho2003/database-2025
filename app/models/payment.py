import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    payment = Column(String(30), nullable=False) 
    
    store = relationship('Store', back_populates='payments')