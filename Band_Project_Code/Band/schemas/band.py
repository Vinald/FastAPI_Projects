from datetime import date
from pydantic import BaseModel, field_validator
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
    GRUNGE = "grunge"


class GenreChoice(Enum):
    ROCK = "Rock"
    POP = "Pop"
    JAZZ = "Jazz"
    CLASSICAL = "Classical"
    HIPHOP = "HipHop"
    COUNTRY = "Country"
    ELECTRONIC = "Electronic"
    REGGAE = "Reggae"
    BLUES = "Blues"
    METAL = "Metal"
    GRUNGE = "Grunge"


class Album(BaseModel):
    title: str
    release_year: int


class BandBase(BaseModel):
    name: str
    genre: GenreChoice
    albums: list[Album] = []


class BandCreate(BandBase):
    @field_validator('genre', mode='before')
    @classmethod
    def title_case_genre(cls, v):
        return v.title()


class BandWithID(BandBase):
    id: int