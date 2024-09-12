from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.orm import relationship

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ..database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    is_active = Column(Boolean, default=True)
    # ecommerces = relationship('Ecommerce', secondary='ecommerce_category_association', back_populates='categories')
