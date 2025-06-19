from abc import ABC
from dataclasses import dataclass
from typing import Optional

from duckdb import DuckDBPyConnection
from kuzu import Connection


@dataclass
class Field:
    column: str
    type: str
    alias: Optional[str] = None

    def __post_init__(self):
        if self.alias is None:
            self.alias = self.column


HID = Field(column="H-ID", alias="id", type="INT64")


@dataclass
class Name:
    table_name: str
    node_label: Optional[str] = None

    def __post_init__(self):
        if self.node_label is None:
            self.node_label = self.table_name


class Base(ABC):

    def __init__(self, conn: DuckDBPyConnection):
        self.conn = conn
        super().__init__()

    @property
    def fields(self) -> list[Field]:
        pass

    @property
    def _from(self) -> str:
        pass

    def make_select_stmt(self) -> str:
        def alias_stmt(field: Field) -> str:
            if (
                field.column.lower().startswith("case when")
                or field.type == "DATE"
                or len(field.column.split(".")) > 1
            ):
                return f"{field.column} as {field.alias}"
            else:
                return f'"{field.column}" AS "{field.alias}"'

        aliases = ", ".join([alias_stmt(field) for field in self.fields])
        return f"SELECT {aliases}"

    def pl(self):
        select = self.make_select_stmt()
        query = f"{select} {self._from}"
        try:
            return self.conn.sql(query=query).pl()
        except Exception as e:
            print(query)
            raise e

    def create_node_stmt(self) -> str:
        name = self.__class__.__name__
        start = f"CREATE NODE TABLE {name}("
        fields = ", ".join([f"{f.alias} {f.type}" for f in self.fields])
        end = ", PRIMARY KEY(id))"
        return f"{start}{fields}{end}"

    def insert_nodes(self, kuzu_connection: Connection):
        query = self.create_node_stmt()
        kuzu_connection.execute(query)
        df = self.pl()
        name = self.__class__.__name__
        kuzu_connection.execute(f"COPY {name} FROM df")
        nodes = kuzu_connection.execute(f"MATCH (n:{name}) RETURN n.*").get_as_pl()
        # Confirm that all the rows in the SQL relation were
        # inserted into the Kuzu nodes table
        assert df.shape == nodes.shape
