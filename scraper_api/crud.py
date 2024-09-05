from sqlalchemy.orm import Session
from . import models, schemas

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.value = item.value
        db.commit()
        db.refresh(db_item)
    return db_item