from fastapi import FastAPI
from .routers import category

app = FastAPI()

# app.include_router(ecommerce.router, prefix="/ecommerce", tags=["ecommerce"])
app.include_router(category.router, prefix="/category", tags=["category"])
# app.include_router(location.router, prefix="/location", tags=["location"])
