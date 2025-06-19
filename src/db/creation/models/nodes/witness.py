from ._base import HID, Base, Field


class Witness(Base):
    fields = [
        HID,
        Field(
            column="case when is_unobserved like 'Yes' then true else false end",
            alias="is_unobserved",
            type="BOOLEAN",
        ),
        Field(column="preferred_siglum", alias="siglum", type="STRING"),
        Field(column="alternative_sigla", type="STRING[]"),
        Field(column="status_witness", alias="status", type="STRING"),
        Field(
            column="case when is_excerpt like 'Yes' then true else false end",
            alias="is_excerpt",
            type="BOOLEAN",
        ),
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
        Field(column="number_of_hands", type="DOUBLE"),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
    ]

    _from = "FROM Witness"
