from src.db import KuzuDB
from src.trees.builders.witness import WitnessTreeBuilder


def test_witness_in_multiple_manuscripts(kuzu_db: KuzuDB):
    # Get the ID of a witness that's in multiple manuscripts
    query = """
MATCH (w:Witness)-[*]->(d:Document)
WITH count(d) AS docs, w as wit
WHERE docs > 1
RETURN wit.id, docs
ORDER BY wit.id
LIMIT 1
"""
    id, expected_count = kuzu_db.get_rows(query)[0]

    # Run the test
    wtb = WitnessTreeBuilder(db=kuzu_db)
    witness = list(wtb.iter_witnesses(witness_id=id))[0]
    actual_count = len(witness.manuscripts)
    assert actual_count == expected_count


def test_witness_with_scripta(kuzu_db: KuzuDB):
    # Get the ID of a witness that has a scripta
    query = """
MATCH (w:Witness)-[]->(s:Scripta)
RETURN w.id
ORDER BY w.id
LIMIT 1
"""
    id = kuzu_db.get_rows(query)[0][0]

    # Run the test
    wtb = WitnessTreeBuilder(db=kuzu_db)
    witness = list(wtb.iter_witnesses(witness_id=id))[0]
    assert witness.scripta.id is not None


def test_witness_in_document_without_repo(kuzu_db: KuzuDB):
    # Get the ID of a witness that's in a document without a repository
    query = """
MATCH (w:Witness)-[*]->(d:Document)
WHERE NOT (d)-[]->(:Repository)
RETURN w.id
ORDER BY w.id
LIMIT 1
"""

    id = kuzu_db.get_rows(query)[0][0]

    # Run the test
    wtb = WitnessTreeBuilder(db=kuzu_db)
    witness = list(wtb.iter_witnesses(witness_id=id))[0]
    assert witness.manuscripts[0].repository is None


def test_witness_in_document_with_repo(kuzu_db: KuzuDB):
    # Get the ID of a witness that's in a document without a repository
    query = """
MATCH (w:Witness)-[*]->(:Document)-[]->(:Repository)
RETURN w.id
ORDER BY w.id
LIMIT 1
"""

    id = kuzu_db.get_rows(query)[0][0]

    # Run the test
    wtb = WitnessTreeBuilder(db=kuzu_db)
    witness = list(wtb.iter_witnesses(witness_id=id))[0]
    assert witness.manuscripts[0].repository.id is not None
