from typing import List, Optional

from pydantic import BaseModel, Field


class Part(BaseModel):
    # Properties of the Part node
    id: int
    div_order: int
    number_of_verses: Optional[int] = Field(default=None)
    part_of_text: Optional[str] = Field(default=None)
    volume_number: Optional[str] = Field(default=None)
    number_of_lines: Optional[int] = Field(default=None)
    verses_per_line: Optional[str] = Field(default=None)
    lines_are_incomplete: Optional[str] = Field(default=None)
    page_ranges: List[Optional[str]] = Field(default=[])
    material: Optional[str] = Field(default=None)
    form: Optional[str] = Field(default=None)
    folio_size_height: Optional[str] = Field(default=None)
    folio_size_width: Optional[str] = Field(default=None)
    estimated_folio_size_height: Optional[str] = Field(default=None)
    estimated_folio_size_width: Optional[str] = Field(default=None)
    writing_surface_area_height: Optional[str] = Field(default=None)
    writing_surface_area_width: Optional[str] = Field(default=None)
    number_of_columns: Optional[str] = Field(default=None)
    above_top_line: Optional[str] = Field(default=None)
    script_type: Optional[str] = Field(default=None)
    subscript_type: Optional[str] = Field(default=None)
    amount_of_illustrations: Optional[str] = Field(default=None)
    has_initials: bool
    has_rubrication: bool
    has_incomplete_decoration: bool
    has_no_decoration: bool
    has_pictorial_designs: bool
    decoration_is_unknown: bool
