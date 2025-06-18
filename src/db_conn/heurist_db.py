from pathlib import Path

import duckdb

from src.config import settings


class HeuristDB:
    def __init__(self, fp: Path = settings.DUCKDB_PATH, read_only: bool = False):
        self.conn = duckdb.connect(database=fp, read_only=read_only)

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
