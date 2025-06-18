from pathlib import Path

import kuzu

from src.config import settings


class KuzuDB:
    def __init__(self, fp: Path = settings.KUZU_PATH, read_only: bool = False):
        db = kuzu.Database(database_path=fp, read_only=read_only)
        self.conn = kuzu.Connection(database=db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def execute(self, query: str, parameters: dict = {}) -> kuzu.QueryResult:
        return self.conn.execute(query=query, parameters=parameters)

    def get_rows(self, query: str, parameters: dict = {}) -> list:
        result = self.execute(query=query, parameters=parameters)
        rows = []
        while result.has_next():
            values = result.get_next()
            rows.append(values)
        return rows
