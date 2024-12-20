from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_pwd: str
    db_usr: str
    port: int

    # JWT Token Related
    secret_key: str
    refresh_secret_key : str
    algorithm: str
    timeout: int
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_MINUTES : int

    # internal env
    adminapikey: str

    SERVER: str

    class Config:
        env_file = Path(__file__).resolve().parent / ".env"


setting = Settings()
