from ._base import Base, Edge


class IsEmbodiedIn(Base):
    edges = [Edge("Text", "Witness")]
    _attr = "lrm"

    selections = [
        """
SELECT
    "is_manifestation_of H-ID" AS "from",
    "H-ID" AS "to",
    'R4' AS lrm
FROM Witness
WHERE "from" IS NOT NULL
    """,
    ]
