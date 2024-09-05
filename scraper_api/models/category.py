from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship
from scraper_api.database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    is_active = Column(Boolean, default=True)
    # ecommerces = relationship('Ecommerce', secondary='ecommerce_category_association', back_populates='categories')
