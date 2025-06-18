from src.build_db.models import edges, nodes
from src.build_db.models.edges._base import Base as EdgeBase
from src.build_db.models.nodes._base import Base as NodeBase
from src.db_conn import HeuristDB, KuzuDB

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


def rebuild_graph(kuzu_db: KuzuDB, heurist_db: HeuristDB):
    with kuzu_db as kuzu_conn, heurist_db as duckdb_conn:
        # Delete all relationships, then delete all nodes
        for rel in EDGES + NODES:
            label = rel.__name__
            query = f"DROP TABLE IF EXISTS {label}"
            kuzu_conn.execute(query=query)

        # Create the new nodes and relationships
        for node in NODES:
            node_table = node(conn=duckdb_conn)
            node_table.insert_nodes(kuzu_conn)

        for edge in EDGES:
            rel_table = edge(conn=duckdb_conn)
            rel_table.insert_edges(kuzu_conn)
