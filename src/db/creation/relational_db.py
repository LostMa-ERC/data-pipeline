from heurist.api.connection import HeuristAPIConnection
from heurist.workflows.etl import extract_transform_load

from src.config import settings
from src.db.connections import HeuristDB


def create_duckdb(conn: HeuristDB):

    # Rewrite the tables in the DuckDB database with new data requested from Heurist
    with HeuristAPIConnection(
        db="jbcamps_gestes",
        login=settings.HEURIST_LOGIN,
        password=settings.HEURIST_PASSWORD,
    ) as client:
        extract_transform_load(
            client=client,
            duckdb_connection=conn,
            record_group_names=["My record types", "Place, features"],
        )
