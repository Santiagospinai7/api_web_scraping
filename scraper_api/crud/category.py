from sqlalchemy.orm import Session
from ..models.category import Category
from ..schemas.category import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    print('category:', category)
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    # Add an ORDER BY clause to ensure results are sorted
    return db.query(Category).order_by(Category.id).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db.delete(db_category)
    db.commit()
    return db_category

