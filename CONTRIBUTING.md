# Contributing 🤖

Because this pipeline is specially designed for LostMa's data needs, contributions are not expected from the broader community.

However, if you would like to contribute to the underlying open-source tool that performs the first step, collecting data from Heurist, see `heurist-api`'s [GitHub repository](https://github.com/LostMa-ERC/heurist-api) for details on contributing.

## Graph solution: [Kùzu](https://kuzudb.com/)

Because the LostMa data is so networked, sometimes it is easier to query as a graph than as relational tables. We've chosen the Graph Database Management System (GBMS) [`Kùzu`](https://kuzudb.com/), which is embedded (like SQLite and DuckDB) and therefore easier to set up and manage.

This young open-source project has good [documentation](https://docs.kuzudb.com/) on their site, as well as a [blog](https://blog.kuzudb.com/). You can also join their [Discord](https://discord.gg/jw7xN2ZhJB) server to pose questions to the maintainers and other users, as well as learn from the discussions others have had there.

## Set up dev environment

Download an editable version of the project with its development dependencies.

```shell
$ pip install -e .[dev]
```

## Testing

When you're developping a behavior that's import to the overall architecture and/or workflow of the project--aka, the pipeline would break or the data would be corrupted if it stopped working as expected--develop a test that confirms the behavior.

See examples in [`tests/`](./tests/).

### Pytest

This project benefits from [pytest](https://docs.pytest.org/en/stable/), which has been preconfigured in the [`pyproject.toml`](pyproject.toml)'s `tool.pytest.ini_options` table and comes downloaded with `pip install -e .[dev]`.

To run all tests:

```
$ pytest
```

To skip the longer end-to-end tests ([`tests/e2e`](./tests/e2e/)) and just run the unit tests:

```
$ pytest tests/unit
```

### Database connection dependencies

Many tests will require connections to the databases created during the pipeline's first 2 steps. These connection objects can be used in all tests by simply requiring the named paramter in the test's function declaration.

```python
def test_something_that_needs_graph_db(kuzu_db):
    query = "MATCH (w:Witness) RETURN w"
    query_result = kuzu_db.execute(query)
```

This is possible thanks to pytest's `@fixture` feature, which is used in the file [`tests/conftest.py`](./tests/conftest.py) to create a database connection / session at the start of every test suite.

```python
from collections.abc import Generator
import pytest
from src.db import KuzuDB


@pytest.fixture(scope="session", autouse=True)
def kuzu_db() -> Generator[KuzuDB, None, None]:
    with KuzuDB(fp=settings.KUZU_PATH) as db_session:
        yield db_session
```

The trick is naming your test's parameter the name of the fixture function, i.e. `kuzu_db`, as it is defined in [`conftest.py`](./tests/conftest.py).

## Modelling tables (relational) to nodes & edges (graph)

You might want to edit the modelling of the graph database, the process of converting the tabular data to nodes and edges.

This modelling is controlled by Python classes in the directory [`src/db/creation/models`](./src/db/creation/models/).

### [Nodes](./src/db/creation/models/nodes/)

Nodes need data fields (list of `Field` named tuples) and the "from" part of an SQL statement (`_from`), which is used to select the data fields from the relevant table / joined tables in the DuckDB database.

The data field (`Field`) named tuple has the following attributes:

- `column` [required] : the name of the column or the select statement (i.e. `case when... then... end`) used to select the data.
- `alias` [optional] : the name of the property as it will be applied to the node; if it's the same as `column` (i.e. the name of a column), the latter will be used and it's not necessary to declare it.
- `type` [required] : the [Kùzu data type](https://docs.kuzudb.com/cypher/data-types/) that the data field will have on the node

```python
from ._base import HID, Base, Field

class Genre(Base):
    fields = [
        HID,
        Field(column="preferred_name", alias="name", type="STRING"),
        Field(column="alternative_names", type="STRING[]"),
        Field(column="description", type="STRING"),
        Field(column="archetype", type="STRING"),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
    ]

    _from = "FROM Genre"

```

Each node needs to have a field `id`, which the `Base` node class uses to create a primary key. Many Heurist entities' unique IDs are selected in the same way: `Field(column="H-ID", alias="id", type="INT64")`. Therefore, a constant `HID` is made available in the [`nodes/_base`](./src/db/creation/models/nodes/_base.py) module.


### [Edges](./src/db/creation/models/edges/)

In a way, edges are more complex to model than nodes because they can connect multiple pairs of node types. For this reason, the `Base` edge class requires ordered lists for its two attributes: `edges` and `selections`.

Each `Edge` dataclass in the list of `edges` takes (1) the name of the "from" node and (2) the name of the "to" node. Node names are identical to the name of the class used to create the node in [`models/nodes`](./src/db/creation/models/nodes/).

Each string in the list of `selections` is a full SQL statement that selects the "from" and "to" data fields to be used for the edges.

> Note: In the SQL statement, it is necessary to not select rows that don't have the foreign key. It might also be necessary to `unnest` a foreign key's values if the Heurist schema allows the entity to have a list of foreign keys. The "to" foreign key must be an integer, which must be the `id` of an existing node in the graph database.

```python
from ._base import Base, Edge

class HasGenre(Base):
    edges = [Edge("Text", "Genre")]

    selections = [
        """
SELECT
    "H-ID" AS "from",
    "specific_genre H-ID" AS "to"
FROM TextTable
WHERE "to" IS NOT NULL
"""
    ]

```
