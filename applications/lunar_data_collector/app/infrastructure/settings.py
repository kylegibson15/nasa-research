from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    nasa_api_key: str
    nasa_tech_port_url: str = "https://techport.nasa.gov/api/projects"
    nasa_lunar_samples_url: str = "https://curator.jsc.nasa.gov/rest/lunarapi/samples"
    # nasa_techtransfer_url = f"https://api.nasa.gov/techtransfer/patent/?engine&api_key={nasa_api_key}"

    postgres_password: str
    postgres_user: str
    postgres_db: str

    pg_dsn: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/nasa_research"
    pg_async_dsn: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/nasa_research"

    class Config:
        env_file = ".env"
