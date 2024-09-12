from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import category as crud_category
from ..schemas.category import CategoryCreate, Category
from ..dependencies import get_db
from typing import List

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

@router.get("/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        categories = crud_category.get_categories(db, skip=skip, limit=limit)
        return categories
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    return crud_category.update_category(db, category_id, category)

@router.delete("/{category_id}", response_model=Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud_category.delete_category(db, category_id)
