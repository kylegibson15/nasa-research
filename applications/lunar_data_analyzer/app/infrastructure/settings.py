from pydantic_settings import BaseSettings


class Settings(BaseSettings):    
    # postgres_password: str
    # postgres_user: str
    # postgres_db: str

    # pg_async_dsn: str

    queue_url: str

    class Config:
        env_file = ".env"
