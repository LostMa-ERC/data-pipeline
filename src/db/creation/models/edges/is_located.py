from ._base import Base, Edge


class IsLocated(Base):
    edges = [Edge("Document", "Repository"), Edge("Repository", "Place")]

    selections = [
        """
SELECT
    "H-ID" AS "from",
    "location H-ID" AS "to"
FROM DocumentTable
WHERE "to" IS NOT NULL
""",
        """
SELECT
    "H-ID" AS "from",
    "city H-ID" AS "to"
FROM Repository
WHERE "to" IS NOT NULL
""",
    ]
