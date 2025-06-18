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
