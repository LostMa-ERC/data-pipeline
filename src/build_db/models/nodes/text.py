from ._base import HID, Base, Field


class Text(Base):
    fields = [
        HID,
        Field(column="preferred_name", alias="name", type="STRING"),
        Field(column="alternative_names", type="STRING[]"),
        Field(column="literary_form", alias="form", type="STRING"),
        Field(
            column="case when is_hypothetical like 'Yes' then true else false end",
            alias="is_hypothetical",
            type="BOOLEAN",
        ),
        Field(
            column="case when peripheral like 'Yes' then true else false end",
            alias="peripheral",
            type="BOOLEAN",
        ),
        Field(column="length", type="DOUBLE"),
        Field(column="verse_type", type="STRING[]"),
        Field(column="rhyme_type", type="STRING[]"),
        Field(column="Stanza_type", alias="stanza_type", type="STRING"),
        Field(column="nature_of_derivations", type="STRING"),
        Field(column="tradition_status", alias="status", type="STRING"),
        Field(column="status_notes", type="STRING"),
        Field(
            column="date_of_creation.estMinDate",
            alias="creation_date_min",
            type="DATE",
        ),
        Field(
            column="date_of_creation.estMaxDate",
            alias="creation_date_max",
            type="DATE",
        ),
        Field(
            column="date_of_creation.value",
            alias="creation_date_year",
            type="DATE",
        ),
        Field(
            column="date_of_creation_certainty",
            alias="creation_date_certainty",
            type="STRING",
        ),
        Field(column="date_freetext", alias="creation_date_text", type="STRING"),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
    ]

    _from = """FROM TextTable"""
