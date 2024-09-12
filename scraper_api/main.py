import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import FastAPI
from .routers import category

app = FastAPI()

# app.include_router(ecommerce.router, prefix="/ecommerce", tags=["ecommerce"])
app.include_router(category.router, prefix="/category", tags=["category"])
# app.include_router(location.router, prefix="/location", tags=["location"])
