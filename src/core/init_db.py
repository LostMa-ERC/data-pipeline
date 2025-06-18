from src.build_db.graph_db import rebuild_graph
from src.build_db.relational_db import refresh_data
from src.db_conn import HeuristDB, KuzuDB
from src.static_files.witness_trees import build_witness_trees


def init_db():
    with HeuristDB() as dconn, KuzuDB() as kconn:
        # Download new data from Heurist
        refresh_data(conn=dconn)

        # Convert the relational database into a Kùzu graph database
        rebuild_graph(kuzu_db=kconn, heurist_db=dconn)

    # Build static witness trees
    build_witness_trees()
