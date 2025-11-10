import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from app.databases.database import Base

class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    category = Column(String(30), nullable=False)
    
    stores = relationship('Store', back_populates='category_info')