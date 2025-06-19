from ._base import HID, Base, Field


class Story(Base):
    fields = [
        HID,
        Field(column="preferred_name", alias="name", type="STRING"),
        Field(column="alternative_names", type="STRING[]"),
        Field(column="matter", type="STRING"),
        Field(
            column="case when peripheral like 'Yes' then true else false end",
            alias="peripheral",
            type="BOOLEAN",
        ),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
    ]

    _from = """FROM Story"""
