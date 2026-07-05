import os
from collections.abc import Generator
from pathlib import Path


os.environ["APP_ENV"] = "test"
os.environ["DATABASE_NAME"] = "agent_platform_test"
os.environ["LOG_LEVEL"] = "WARNING"
os.environ["LOG_DIR"] = "./.test-logs"
os.environ["STORAGE_DIR"] = "./.test-storage"


import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db.session import engine, get_db
from app.main import app


BACKEND_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session", autouse=True)
def migrated_test_database() -> None:
    if engine.url.database != "agent_platform_test":
        raise RuntimeError(
            "Tests must run against agent_platform_test"
        )

    alembic_config = Config(BACKEND_DIR / "alembic.ini")
    command.upgrade(alembic_config, "head")


@pytest.fixture
def db_session(
    migrated_test_database: None,
) -> Generator[Session, None, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(
    db_session: Session,
) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
