from pathlib import Path
from pydantic_settings import BaseSettings


# Resolve project root reliably
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "models/gemini-2.5-flash-lite"
    GEMINI_TEMPERATURE: float = 0.0

    model_config = {
        "env_file": PROJECT_ROOT / ".env",
        "extra": "ignore",
    }


settings = Settings()
