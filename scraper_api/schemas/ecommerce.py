from pydantic import BaseModel
from typing import List

class EcommerceBase(BaseModel):
    name: str
    url: str

class EcommerceCreate(EcommerceBase):
    categories: List[int]
    locations: List[int]

class Ecommerce(EcommerceBase):
    id: int
    class Config:
        orm_mode = True
        