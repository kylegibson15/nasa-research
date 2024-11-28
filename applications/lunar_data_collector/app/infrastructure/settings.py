from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    nasa_api_key: str
    nasa_tech_port_url: str = "https://techport.nasa.gov/api/projects"
    nasa_tech_port_swagger_url: str = "https://techport.nasa.gov/help/api"
    nasa_lunar_samples_url: str = "https://curator.jsc.nasa.gov/rest/lunarapi/samples"
    # nasa_techtransfer_url = f"https://api.nasa.gov/techtransfer/patent/?engine&api_key={nasa_api_key}"
    
    postgres_password: str
    postgres_user: str
    postgres_db: str

    pg_async_dsn: str

    queue_url: str

    class Config:
        env_file = ".env"
