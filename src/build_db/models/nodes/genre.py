from ._base import HID, Base, Field


class Genre(Base):
    fields = [
        HID,
        Field(column="preferred_name", alias="name", type="STRING"),
        Field(column="alternative_names", type="STRING[]"),
        Field(column="description", type="STRING"),
        Field(column="archetype", type="STRING"),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
    ]

    _from = "FROM Genre"
