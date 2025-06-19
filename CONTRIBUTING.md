# Contributing 🤖

Because this pipeline is specially designed for LostMa's data needs, contributions are not expected from the broader community.

However, if you would like to contribute to the underlying open-source tool that performs the first step, collecting data from Heurist, see `heurist-api`'s [GitHub repository](https://github.com/LostMa-ERC/heurist-api) for details on contributing.

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
    # etc.
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
