from typing import List, Optional

from pydantic import BaseModel, Field

from src.models.part import Part
from src.models.repository import Repository


class Document(BaseModel):
    # Properties of the Document node
    id: int
    shelfmark: Optional[str] = Field(default=None)
    old_shelfmarks: List[Optional[str]] = Field(default=[])
    collection: Optional[str] = Field(default=None)
    is_hypothetical: bool
    collection_of_fragments: Optional[str] = Field(default=None)
    urls: List[Optional[str]] = Field(default=[])
    ark: Optional[str] = Field(default=None)

    # Nested nodes
    witness_parts: List[Optional[Part]] = Field(default=[])
    repository: Optional[Repository] = Field(default=None)
