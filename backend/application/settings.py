from pydantic import AnyHttpUrl, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str | None = "bewise-redis"
    REDIS_PORT: int | None = 6379
    REDIS_PASSWORD: str | None = "qwerty"

    @property
    def REDIS_URL(self) -> RedisDsn:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


class PostgresSettings(BaseSettings):
    POSTGRES_NAME: str | None = "postgres"
    POSTGRES_USER: str | None = "postgres"
    POSTGRES_PASSWORD: str | None = "postgres"
    POSTGRES_SERVER: str | None = "bewise-db"
    POSTGRES_PORT: int | None = 9991

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_NAME or ''}"
        )


class Settings(RedisSettings, PostgresSettings):
    API_V1_STR: str = "/api"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    SERVICE_URL: str = "https://jservice.io/api/random"


settings: Settings = Settings()
