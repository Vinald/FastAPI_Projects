from fastapi import FastAPI

from .api.v1.band import band_router

app = FastAPI()

app.include_router(band_router, prefix="/bands", tags=["bands"])
