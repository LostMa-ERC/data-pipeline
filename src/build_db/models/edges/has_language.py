from ._base import Base, Edge


class HasLanguage(Base):
    edges = [Edge("Text", "Language"), (Edge("Scripta", "Language"))]

    selections = [
        """
SELECT
    "H-ID" as "from",
    "language_COLUMN TRM-ID" as "to"
FROM TextTable
WHERE "to" IS NOT NULL
""",
        """
SELECT
    "H-ID" as "from",
    "language_COLUMN TRM-ID" as "to"
FROM Scripta
WHERE "to" IS NOT NULL
""",
    ]
