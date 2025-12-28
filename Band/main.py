from .api.v1.band import band_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(band_router, prefix="/bands", tags=["bands"])
