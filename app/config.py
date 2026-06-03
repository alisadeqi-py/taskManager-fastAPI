from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:123456@localhost/tasksdb"

    class Config:
        env_file = ".env"

settings = Settings()