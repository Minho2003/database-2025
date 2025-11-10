import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Order(Base):
    __tablename__ = 'order' 
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    rider_id = Column(Integer, ForeignKey('rider.id'), nullable=False)
    order_details = Column(String(100), name='order', nullable=False) 
    total_price = Column(Integer, nullable=False)
    order_time = Column(DateTime, nullable=False, default=func.now())
    
    user = relationship('User', back_populates='orders')
    store = relationship('Store', back_populates='orders')
    rider = relationship('Rider', back_populates='orders')