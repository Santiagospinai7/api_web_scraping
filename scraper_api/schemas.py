from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    value: int

class ShopCreate(BaseModel):
    name: str
    url: str
    price: int
    is_active: bool = True