from typing import Optional

from pydantic import BaseModel, Field


class Place(BaseModel):
    id: int
    name: str
    region: Optional[str] = Field(default=[])
    country: Optional[str] = Field(default=None)
    place_type: Optional[str] = Field(default=None)
    location_mappable: Optional[str] = Field(default=None)
    location_certainty: Optional[str] = Field(default=None)
    geonames_id: Optional[int] = Field(default=None)
