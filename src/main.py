import click

from src.config import settings
from src.db.connections import HeuristDB, KuzuDB
from src.db.creation import create_duckdb, create_kuzudb
from src.db.init_db import init_db
from src.trees.witness_trees import build_witness_trees


@click.group()
def cli():
    pass


@cli.group("build")
def build():
    pass


@build.command("full")
def build_full():
    init_db(duckdb_path=settings.DUCKDB_PATH, kuzu_path=settings.KUZU_PATH)


@build.command("heurist")
def build_heurist():
    with HeuristDB(fp=settings.DUCKDB_PATH) as conn:
        create_duckdb(conn=conn)


@build.command("graph")
def build_graph():
    with (
        KuzuDB(fp=settings.KUZU_PATH) as kdb,
        HeuristDB(fp=settings.DUCKDB_PATH) as dconn,
    ):
        create_kuzudb(kuzu_db=kdb, duckdb_conn=dconn)


@build.command("witness")
@click.option("-t", "--type", type=click.Choice(choices=["json"]))
def build_witness(type: str):
    with KuzuDB(fp=settings.KUZU_PATH) as db:
        if type == "json":
            build_witness_trees(db=db)


if __name__ == "__main__":
    cli()
