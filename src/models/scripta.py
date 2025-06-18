from typing import List, Optional

from pydantic import BaseModel, Field


class Scripta(BaseModel):
    id: int
    name: str
    description: Optional[str] = Field(default=None)
    urls: List[Optional[str]] = Field(default=[])
