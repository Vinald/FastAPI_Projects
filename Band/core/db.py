import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///./band.sqlite3"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
