import pytest

from src.db.creation import create_duckdb, create_kuzudb
from src.trees.witness_trees import build_witness_trees


@pytest.mark.dependency()
def test_heurist_build(duckdb_conn):
    create_duckdb(conn=duckdb_conn)


@pytest.mark.dependency(depends=["test_heurist_build"])
def test_graph_build(kuzu_db, duckdb_conn):
    create_kuzudb(kuzu_db=kuzu_db, duckdb_conn=duckdb_conn)


@pytest.mark.dependency(depends=["test_graph_build"])
def test_witness_json_trees(kuzu_db):
    build_witness_trees(db=kuzu_db)
