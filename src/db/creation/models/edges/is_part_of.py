from ._base import Base, Edge


class IsPartOf(Base):
    edges = [Edge("Storyverse", "Storyverse"), Edge("Story", "Storyverse")]

    selections = [
        """
SELECT
    "H-ID" AS "from",
    unnest("member_of_cycle H-ID") AS "to"
FROM Storyverse
WHERE "member_of_cycle H-ID" != []
""",
        """
SELECT
    "H-ID" AS "from",
    unnest("is_part_of_storyverse H-ID") AS "to"
FROM Story
WHERE "is_part_of_storyverse H-ID" != []
""",
    ]
