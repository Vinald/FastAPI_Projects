from fastapi import APIRouter
from data import BANDS
from schemas import GenreURLChoice, BandBase, BandCreate, BandWithID

band_router = APIRouter()


@band_router.get("/")
async def get_bands(genre: GenreURLChoice | None = None) -> list[BandWithID]:
    if genre:
        return [band for band in BANDS if band["genre"].lower() == genre.value.lower()]
    return BANDS


@band_router.get("/{band_id}")
async def get_band(band_id: int) -> BandWithID:
    band = next((band for band in BANDS if band["id"] == band_id), None)
    if band:
        return band
    return BandWithID(id=band_id)


@band_router.get("/genre/{genre}")
async def get_bands_by_genre(genre: GenreURLChoice) -> list[dict]:
    return [band for band in BANDS if band["genre"].lower() == genre.value.lower()]


@band_router.post("/")
async def create_band(band: BandCreate) -> BandWithID:
    new_id = max(band["id"] for band in BANDS) + 1 if BANDS else 1
    new_band = band.model_dump()
    new_band["id"] = new_id
    BANDS.append(new_band)
    return BandWithID(**new_band)