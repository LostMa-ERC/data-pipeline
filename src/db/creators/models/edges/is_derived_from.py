from ._base import Base, Edge


class IsDerivedFrom(Base):
    edges = [Edge("Story", "Story"), Edge("Text", "Text")]

    selections = [
        """
SELECT
    "H-ID" AS "from",
    unnest("is_modeled_on H-ID") AS "to"
FROM Story
WHERE "is_modeled_on H-ID" != []
""",
        """
SELECT
    "H-ID" AS "from",
    unnest("is_derived_from H-ID") AS "to"
FROM TextTable
WHERE "is_derived_from H-ID" != []
""",
    ]
