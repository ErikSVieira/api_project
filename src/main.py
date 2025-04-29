from fastapi import FastAPI
from src.core.database import Base, engine
from src.routers import products_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products_router.router)
