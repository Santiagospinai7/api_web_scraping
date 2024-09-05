from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

ecommerce_category_association = Table(
    'ecommerce_categories',
    Base.metadata,
    Column('ecommerce_id', Integer, ForeignKey('ecommerces.id')),
    Column('category_id', Integer, ForeignKey('categories.id')),
    Column('is_active', bool, default=True)
)

ecommerce_location_association = Table(
    'ecommerce_locations',
    Base.metadata,
    Column('ecommerce_id', Integer, ForeignKey('ecommerces.id')),
    Column('location_id', Integer, ForeignKey('locations.id')),
    Column('is_active', bool, default=True)
)

class Ecommerce(Base):
    __tablename__ = 'ecommerces'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    url = Column(String(255), index=True)
    is_active = Column(bool, default=True)
    categories = relationship('Category', secondary=ecommerce_category_association, back_populates='ecommerces')
    locations = relationship('Location', secondary=ecommerce_location_association, back_populates='ecommerces')