from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api.v1.band import band_router
from .core.db import init_db


@asynccontextmanager
async def lifespan(apps: FastAPI):
    init_db()
    yield
    # Shutdown code here


app = FastAPI(lifespan=lifespan)

app.include_router(band_router, prefix="/bands", tags=["bands"])
