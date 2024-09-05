from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    is_active = Column(bool, default=True)
    ecommerces = relationship('Ecommerce', secondary='ecommerce_location_association', back_populates='locations')
