from ._base import Base, Edge


class HasWritingStyle(Base):
    edges = [Edge("Text", "Scripta"), Edge("Witness", "Scripta")]

    selections = [
        """
SELECT
    "H-ID" AS "from",
    "regional_writing_style H-ID" AS "to"
FROM TextTable
WHERE "to" IS NOT NULL
""",
        """
SELECT
    "H-ID" AS "from",
    "regional_writing_style H-ID" AS "to"
FROM Witness
WHERE "to" IS NOT NULL
""",
    ]
