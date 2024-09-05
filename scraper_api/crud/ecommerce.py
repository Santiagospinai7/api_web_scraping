from sqlalchemy.orm import Session
from ..models.ecommerce import Ecommerce
from ..schemas.ecommerce import EcommerceCreate

def create_ecommerce(db: Session, ecommerce: EcommerceCreate):
    db_ecommerce = Ecommerce(name=ecommerce.name, url=ecommerce.url)
    db.add(db_ecommerce)
    db.commit()
    db.refresh(db_ecommerce)
    return db_ecommerce

def get_ecommerce(db: Session, ecommerce_id: int):
    return db.query(Ecommerce).filter(Ecommerce.id == ecommerce_id).first()

def get_ecommerces(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ecommerce).offset(skip).limit(limit).all()
