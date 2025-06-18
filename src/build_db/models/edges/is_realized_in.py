from ._base import Base, Edge


class IsRealizedIn(Base):
    edges = [Edge("Story", "Text")]
    _attr = "lrm"

    selections = [
        """
SELECT
    unnest("is_expression_of H-ID") AS "from",
    "H-ID" AS "to",
    'R3' AS lrm
FROM TextTable
WHERE "is_expression_of H-ID" != []
"""
    ]
