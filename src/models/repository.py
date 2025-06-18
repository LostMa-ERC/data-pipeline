from typing import List, Optional

from pydantic import BaseModel, Field

from src.models.place import Place


class Repository(BaseModel):
    # Properties of the Repository node
    id: int
    name: str
    alternative_names: List[Optional[str]] = Field(default=[])
    viaf: Optional[str] = Field(default=[])
    isni: Optional[str] = Field(default=[])
    biblissima_identifier: Optional[str] = Field(default=[])
    website: Optional[str] = Field(default=[])

    # Nested nodes
    settlement: Optional[Place] = Field(default=None)
