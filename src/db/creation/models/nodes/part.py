from ._base import Base, Field


class Part(Base):
    fields = [
        Field(column='pt."H-ID"', alias="id", type="INT64"),
        Field(column="pt.div_order", alias="div_order", type="INT8"),
        Field(column="pt.number_of_verses", alias="number_of_verses", type="INT64"),
        Field(column="pt.part_of_text", alias="part_of_text", type="STRING"),
        Field(column="pt.volume_number", alias="volume_number", type="STRING"),
        Field(column="pt.number_of_lines", alias="number_of_lines", type="INT64"),
        Field(column="pt.verses_per_line", alias="verses_per_line", type="STRING"),
        Field(
            column="pt.lines_are_incomplete",
            alias="lines_are_incomplete",
            type="STRING",
        ),
        Field(column="pt.page_ranges", alias="page_ranges", type="STRING[]"),
        Field(column="pd.material", alias="material", type="STRING"),
        Field(column="pd.form", alias="form", type="STRING"),
        Field(column="pd.folio_size_height", alias="folio_size_height", type="STRING"),
        Field(column="pd.folio_size_width", alias="folio_size_width", type="STRING"),
        Field(
            column="pd.estimated_folio_size_height",
            alias="estimated_folio_size_height",
            type="STRING",
        ),
        Field(
            column="pd.estimated_folio_size_width",
            alias="estimated_folio_size_width",
            type="STRING",
        ),
        Field(
            column="pd.writing_surface_area_height",
            alias="writing_surface_area_height",
            type="STRING",
        ),
        Field(
            column="pd.writing_surface_area_width",
            alias="writing_surface_area_width",
            type="STRING",
        ),
        Field(column="pd.number_of_columns", alias="number_of_columns", type="STRING"),
        Field(column="pd.above_top_line", alias="above_top_line", type="STRING"),
        Field(column="pd.script_type", alias="script_type", type="STRING"),
        Field(column="pd.subscript_type", alias="subscript_type", type="STRING"),
        Field(
            column="pd.amount_of_illustrations",
            alias="amount_of_illustrations",
            type="STRING",
        ),
        Field(
            column="case when 'initial' in pd.has_decorations then true else false end",
            alias="has_initials",
            type="STRING",
        ),
        Field(
            column="case when 'rubrication' in pd.has_decorations then true else false \
                end",
            alias="has_rubrication",
            type="STRING",
        ),
        Field(
            column="case when 'incomplete dec.' in pd.has_decorations then true else \
                false end",
            alias="has_incomplete_decoration",
            type="STRING",
        ),
        Field(
            column="case when 'no decoration' in pd.has_decorations then true else \
                false end",
            alias="has_no_decoration",
            type="STRING",
        ),
        Field(
            column="case when 'unrelated pictures' in pd.has_decorations then true else\
                false end",
            alias="has_pictorial_designs",
            type="STRING",
        ),
        Field(
            column="case when 'unknown' in pd.has_decorations then true else false end",
            alias="decoration_is_unknown",
            type="STRING",
        ),
    ]

    _from = """
FROM Part pt
LEFT JOIN PhysDesc pd
    ON pt."is_inscribed_on H-ID" = pd."H-ID"
"""
