from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Agent Platform API"
    app_env: Literal["development", "test", "production"] = "development"
    app_debug: bool = False
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    log_dir: Path = BACKEND_DIR / "logs"
    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    storage_dir: Path = BACKEND_DIR / "storage"
    max_upload_size_mb: int = 20
    allowed_document_extensions: list[str] = [".txt", ".pdf", ".md", ".markdown"]
    upload_chunk_size_bytes: int = 1048576


    database_host: str = "127.0.0.1"
    database_port: int = 5432
    database_name: str = "agent_platform"
    database_user: str = "agent_app"
    database_password: SecretStr = SecretStr("")
    database_echo: bool = False
    database_pool_size: int = 5
    database_max_overflow: int = 10

    @model_validator(mode="after")
    def validate_database_password(self) -> Self:
        if not self.database_password.get_secret_value():
            raise ValueError("DATABASE_PASSWORD must not be empty")
        return self

    @field_validator("log_dir", "storage_dir", mode="before")
    @classmethod
    def resolve_backend_path(cls, value: str | Path) -> Path:
        path = Path(value)
        if path.is_absolute():
            return path
        return (BACKEND_DIR / path).resolve()

    @field_validator("max_upload_size_mb", "upload_chunk_size_bytes")
    @classmethod
    def validate_positive_int(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Value must be a positive integer")
        return value

    @property
    def upload_dir(self) -> Path:
        return self.storage_dir / "uploads"

    @property
    def knowledge_dir(self) -> Path:
        return self.storage_dir / "knowledge"

    @property
    def faiss_dir(self) -> Path:
        return self.storage_dir / "faiss"


@lru_cache
def get_settings() -> Settings:
    return Settings()
