import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Owner(Base):
    __tablename__ = 'owner'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(String(30), nullable=False, unique=True)
    owner_passwd = Column(String(50), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    
    stores = relationship('Store', back_populates='owner')