from pydantic_settings import BaseSettings


class Settings(BaseSettings):    
    pg_async_dsn: str

    queue_url: str

    class Config:
        env_file = ".env"
