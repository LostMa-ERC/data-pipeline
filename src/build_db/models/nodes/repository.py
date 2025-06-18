from ._base import HID, Base, Field


class Repository(Base):
    fields = [
        HID,
        Field(column="preferred_name", alias="name", type="STRING"),
        Field(column="alternative_names", alias="alternative_names", type="STRING[]"),
        Field(column="VIAF", alias="viaf", type="STRING"),
        Field(column="ISNI", alias="isni", type="STRING"),
        Field(column="biblissima_identifier", alias="biblissima", type="STRING"),
        Field(column="website", alias="website", type="STRING"),
    ]

    _from = """FROM Repository"""
