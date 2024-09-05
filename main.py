from typing import Union
from scraping import Scraper
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None

class Shop(BaseModel):
  name: str
  location: str
  url: str

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/shop/new")
def create_shop(shop: Shop):
  return shop

@app.get("/shops/")
# Return a list of shops created
def read_shop(shop: Shop):
  return shop

@app.get("/shop/{shop_id}")
def read_cloth(price: float, url: str):
  scraper = Scraper(url, price)
  clothes = scraper.scrape()
  return JSONResponse(content=clothes)
