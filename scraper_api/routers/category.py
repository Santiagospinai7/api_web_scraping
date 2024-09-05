from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import category as crud_category
from ..schemas.category import CategoryCreate, Category
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud_category.create_category(db, category)

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud_category.get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
