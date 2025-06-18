from ._base import HID, Base, Field


class Place(Base):
    fields = [
        HID,
        Field(column="place_name", alias="name", type="STRING"),
        Field(column="administrative_region", alias="region", type="STRING"),
        Field(column="country", type="STRING"),
        Field(column="place_type", type="STRING"),
        Field(column="location_mappable", type="STRING"),
        Field(column="location_certainty", type="STRING"),
        Field(column="geonames_id", type="INT"),
    ]

    _from = "FROM Place"
