from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    OPENROUTER_KEY: str
    ENV: str = "Developement"
    DEBUG: bool = False

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()  # type: ignore
