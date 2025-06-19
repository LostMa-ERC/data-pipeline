from abc import ABC
from dataclasses import dataclass

from duckdb import DuckDBPyConnection
from kuzu import Connection


@dataclass
class Edge:
    _from_node: str
    _to_node: str

    def str(self) -> str:
        return f"FROM {self._from_node} TO {self._to_node}"


class Base(ABC):
    _attr: str | None = None

    def __init__(self, conn: DuckDBPyConnection):
        self.conn = conn
        assert len(self.edges) == len(self.selections)
        super().__init__()

    @property
    def edges(self) -> list[Edge]:
        pass

    @property
    def selections(self) -> str:
        pass

    def create_rel_stmt(self) -> str:
        name = self.__class__.__name__

        def edge_pair(edge: Edge) -> str:
            return f"FROM {edge._from_node} TO {edge._to_node}"

        pairs = ", ".join([edge_pair(edge=edge) for edge in self.edges])
        if self._attr:
            pairs += f", {self._attr} STRING"
        return f"CREATE REL TABLE {name}({pairs})"

    def insert_edges(self, kuzu_connection: Connection):
        name = self.__class__.__name__
        query = self.create_rel_stmt()
        kuzu_connection.execute(query)
        for edge, sql in zip(self.edges, self.selections):

            # Select the data from the relational database
            try:
                rel = self.conn.sql(sql)
                df = rel.pl()
            except Exception as e:
                print(query)
                raise e

            # Insert the data into the graph database
            query = (
                f"COPY {name} FROM df (from='{edge._from_node}', to='{edge._to_node}')"
            )
            try:
                kuzu_connection.execute(query)
            except Exception as e:
                print(query)
                raise e

            # Confirm that all the edges were added
            query = f"""MATCH (a:{edge._from_node})-[r:{name}]->(b:{edge._to_node})
            RETURN a.id, b.id"""
            rels = kuzu_connection.execute(query).get_as_pl()
            assert df.shape[0] == rels.shape[0]
