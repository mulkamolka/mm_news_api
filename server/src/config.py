import logging
import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import AnyUrl, BaseSettings


logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.environ.get("ENVIRONMENT", "dev")  # dev/stage/prod
    testing: bool = os.environ.get("TESTING", 0)  # when test mode, it's 1
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    logger.info("Loading config settings from the environment")
    return Settings()
