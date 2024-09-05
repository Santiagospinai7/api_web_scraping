from sqlalchemy.orm import Session
from ..models.location import Location
from ..schemas.location import LocationCreate

def create_location(db: Session, location: LocationCreate):
    db_location = Location(name=location.name)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Location).offset(skip).limit(limit).all()
