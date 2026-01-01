from enum import Enum

from pydantic import field_validator
from sqlmodel import Field, SQLModel, Relationship


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


class AlbumBase(SQLModel):
    title: str
    release_year: int
    band_id: int | None = Field(foreign_key="band.id")


class BandBase(SQLModel):
    name: str
    genre: GenreChoice


class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: Band = Relationship(back_populates="albums")


class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")


class BandCreate(BandBase):
    album: list[AlbumBase] | None = None

    @field_validator('genre', mode='before')
    @classmethod
    def title_case_genre(cls, v):
        return v.title()
