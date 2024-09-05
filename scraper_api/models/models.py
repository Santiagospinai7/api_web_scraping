from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    value = Column(Integer)

class Shop(Base):
    __schema__ = "ecommerce"
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    url = Column(String(255), index=True)
    price = Column(Integer)
    is_active = Column(Boolean, default=True)