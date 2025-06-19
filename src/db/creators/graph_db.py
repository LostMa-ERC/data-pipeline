from src.db.connections import HeuristDB, KuzuDB
from src.db.creators.models import edges, nodes
from src.db.creators.models.edges._base import Base as EdgeBase
from src.db.creators.models.nodes._base import Base as NodeBase

NODES: list[NodeBase] = [
    nodes.Storyverse,
    nodes.Story,
    nodes.Text,
    nodes.Witness,
    nodes.Part,
    nodes.Document,
    nodes.Repository,
    nodes.Place,
    nodes.Genre,
    nodes.Scripta,
    nodes.Language,
]

EDGES: list[EdgeBase] = [
    edges.IsPartOf,
    edges.IsDerivedFrom,
    edges.IsRealizedIn,
    edges.IsEmbodiedIn,
    edges.HasWritingStyle,
    edges.HasGenre,
    edges.IsMaterializedOn,
    edges.IsLocated,
    edges.HasLanguage,
]


def create_kuzudb(kuzu_db: KuzuDB, duckdb_conn: HeuristDB):
    # Delete all relationships, then delete all nodes
    for rel in EDGES + NODES:
        label = rel.__name__
        query = f"DROP TABLE IF EXISTS {label}"
        kuzu_db.execute(query=query)

    # Create the new nodes and relationships
    for node in NODES:
        node_table = node(conn=duckdb_conn)
        node_table.insert_nodes(kuzu_connection=kuzu_db.conn)

    for edge in EDGES:
        rel_table = edge(conn=duckdb_conn)
        rel_table.insert_edges(kuzu_connection=kuzu_db.conn)
