from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import location as crud_location
from ..schemas.location import LocationCreate, Location
from ..dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Location)
def create_category(location: LocationCreate, db: Session = Depends(get_db)):
    return crud_location.create_location(db, location)

@router.get("/{location_id}", response_model=Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    location = crud_location.get_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.get("/", response_model=List[Location])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        categories = crud_location.get_categories(db, skip=skip, limit=limit)
        return categories
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

