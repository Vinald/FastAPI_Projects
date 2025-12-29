from contextlib import asynccontextmanager

from fastapi import FastAPI

from Band.core.db import init_db
from .api.v1.band import band_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # Shutdown code here


app = FastAPI(lifespan=lifespan)

app.include_router(band_router, prefix="/bands", tags=["bands"])
