import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Rider(Base):
    __tablename__ = 'rider'
    
    id = Column(Integer, primary_key=True)
    rider_id = Column(String(30), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    vehicle = Column(String(30), nullable=False)
    
    # Relationship
    orders = relationship('Order', back_populates='rider')