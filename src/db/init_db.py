from pathlib import Path

from src.trees.witness_trees import build_witness_trees

from .connections import HeuristDB, KuzuDB
from .creation.graph_db import create_kuzudb
from .creation.relational_db import create_duckdb


def init_db(duckdb_path: Path, kuzu_path: Path, databases_only: bool = False) -> None:
    with HeuristDB(fp=duckdb_path) as dconn, KuzuDB(fp=kuzu_path) as kdb:
        # Download new data from Heurist
        create_duckdb(conn=dconn)

        # Convert the relational database into a Kùzu graph database
        create_kuzudb(kuzu_db=kdb, duckdb_conn=dconn)

        if not databases_only:
            # Build static witness trees
            build_witness_trees(db=kdb)
