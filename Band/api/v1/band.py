from typing import Annotated

from fastapi import APIRouter, Path

from Band.data import BANDS
# from Band.core.db import get_session
from Band.model.band import GenreURLChoice, BandCreate, Band

band_router = APIRouter()


def _genre_value(obj) -> str:
    """Return a lowercase genre string whether obj is an Enum or a str."""
    if obj is None:
        return ""
    return obj.value.lower() if hasattr(obj, "value") else str(obj).lower()


@band_router.get("/")
async def get_bands(genre: GenreURLChoice | None = None) -> list[Band]:
    if genre:
        target = _genre_value(genre)
        return [band for band in BANDS if _genre_value(band.get("genre")) == target]
    return BANDS


@band_router.get("/{band_id}")
async def get_band(band_id: Annotated[int, Path(title="This is the band ID", gt=0)]) -> Band:
    band = next((band for band in BANDS if band["id"] == band_id), None)
    if band:
        return band
    return Band(id=band_id)


@band_router.get("/genre/{genre}")
async def get_bands_by_genre(genre: GenreURLChoice) -> list[dict]:
    target = _genre_value(genre)
    return [band for band in BANDS if _genre_value(band.get("genre")) == target]


@band_router.post("/")
async def create_band(band: BandCreate) -> Band:
    new_id = max(item["id"] for item in BANDS) + 1 if BANDS else 1
    new_band = band.model_dump()
    new_band["id"] = new_id
    BANDS.append(new_band)
    return Band(**new_band)
