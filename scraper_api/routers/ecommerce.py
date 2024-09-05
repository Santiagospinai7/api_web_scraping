from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import ecommerce as crud_ecommerce
from ..schemas.ecommerce import EcommerceCreate, Ecommerce
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Ecommerce)
def create_ecommerce(ecommerce: EcommerceCreate, db: Session = Depends(get_db)):
    return crud_ecommerce.create_ecommerce(db, ecommerce)

@router.get("/{ecommerce_id}", response_model=Ecommerce)
def read_ecommerce(ecommerce_id: int, db: Session = Depends(get_db)):
    ecommerce = crud_ecommerce.get_ecommerce(db, ecommerce_id)
    if ecommerce is None:
        raise HTTPException(status_code=404, detail="Ecommerce not found")
    return ecommerce
