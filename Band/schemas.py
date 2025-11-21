from datetime import date
from pydantic import BaseModel
from enum import Enum


class GenreURLChoice(Enum):
    ROCK = "rock"
    POP = "pop"
    JAZZ = "jazz"
    CLASSICAL = "classical"
    HIPHOP = "hiphop"
    COUNTRY = "country"
    ELECTRONIC = "electronic"
    REGGAE = "reggae"
    BLUES = "blues"
    METAL = "metal"


class Album(BaseModel):
    title: str
    release_year: int


class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []


class BandCreate(BandBase):
    pass


class BandWithID(BandBase):
    id: int