from collections.abc import Generator

import pytest

from src.config import settings
from src.db import HeuristDB, KuzuDB
from src.db.init_db import init_db

if not settings.KUZU_PATH.is_dir() or not settings.DUCKDB_PATH.is_file():
    init_db(
        duckdb_path=settings.DUCKDB_PATH,
        kuzu_path=settings.KUZU_PATH,
        databases_only=True,
    )


@pytest.fixture(scope="session", autouse=True)
def kuzu_db() -> Generator[KuzuDB, None, None]:
    with KuzuDB(fp=settings.KUZU_PATH) as db_session:
        yield db_session


@pytest.fixture(scope="session", autouse=True)
def duckdb_conn() -> Generator[HeuristDB, None, None]:
    with HeuristDB(fp=settings.DUCKDB_PATH) as conn:
        yield conn
