from ._base import Base, Edge


class IsMaterializedOn(Base):
    edges = [Edge("Witness", "Part"), Edge("Part", "Document")]
    _attr = "lrm"

    selections = [
        """
SELECT
    "H-ID" AS "from",
    unnest("observed_on_pages H-ID") AS "to",
    'R7' AS lrm
FROM Witness
WHERE "observed_on_pages H-ID" != []
""",
        """
SELECT
    "H-ID" AS "from",
    "is_inscribed_on H-ID" AS "to",
    'R7' AS lrm
FROM Part
WHERE "to" IS NOT NULL
""",
    ]
