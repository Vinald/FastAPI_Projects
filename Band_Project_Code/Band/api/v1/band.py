from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from Band.core.db import get_session
from Band.model.band import BandCreate, Band, Album

band_router = APIRouter()


@band_router.post("/")
async def create_band(band_data: BandCreate, session: Session = Depends(get_session)) -> Band:
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)

    if band_data.album:
        for album_data in band_data.album:
            album_obj = Album(title=album_data.title, release_year=album_data.release_year, band=band)
            session.add(album_obj)

    session.commit()
    session.refresh(band)
    return band


@band_router.get("/")
async def get_all_bands(session: Session = Depends(get_session)):
    bands = session.exec(select(Band)).all()
    return bands


@band_router.get("/{band_id}")
async def get_band(band_id: int, session: Session = Depends(get_session)) -> Band:
    band = session.get(Band, band_id)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

# @band_router.get("/genre/{genre}")
# async def get_bands_by_genre(genre: GenreURLChoice) -> list[dict]:
#     target = _genre_value(genre)
#     return [band for band in BANDS if _genre_value(band.get("genre")) == target]
