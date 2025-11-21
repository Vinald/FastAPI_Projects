from fastapi import FastAPI
from .routes import products_route
from .database import engine
from .schemas import Base

app = FastAPI()

version = "v1.0.0"

Base.metadata.create_all(engine)

app.include_router(products_route, prefix=f"/api/{version}")
