from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PASSWORD: str
    DB_USER: str
    
    class Config:
        env_file = ".env"

settings = Settings()