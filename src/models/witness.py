from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field

from src.models.document import Document
from src.models.scripta import Scripta


class Witness(BaseModel):
    # Properties of the Witness node
    id: int
    is_unobserved: bool
    is_excerpt: bool
    siglum: Optional[str] = Field(default=None)
    alternative_sigla: List[Optional[str]] = Field(default=[])
    status: Optional[str] = Field(default=None)
    creation_date_min: Optional[date] = Field(default=None)
    creation_date_max: Optional[date] = Field(default=None)
    creation_date_year: Optional[date] = Field(default=None)
    creation_date_certainty: Optional[str] = Field(default=None)
    creation_date_text: Optional[str] = Field(default=None)
    number_of_hands: Optional[int] = Field(default=None)
    urls: List[Optional[str]] = Field(default=[])

    # Nested nodes
    scripta: Optional[Scripta] = Field(default=None)  # HasWritingStyle
    manuscripts: List[Optional[Document]] = Field(default=[])  # IsMaterializedOn
