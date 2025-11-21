from routes import band_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(band_router, prefix="/bands", tags=["bands"])
