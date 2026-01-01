from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"

settings = Settings()