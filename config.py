from typing import Optional

from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    LOG_LEVEL: Optional[int] = 30  # logging level - уровень в стандартной библиотеке Logging.
    DB_NAME: Optional[str] = "db.sqlite"


settings = Settings()
