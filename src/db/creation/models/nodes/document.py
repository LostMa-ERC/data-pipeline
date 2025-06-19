from ._base import HID, Base, Field


class Document(Base):
    fields = [
        HID,
        Field(column="current_shelfmark", alias="shelfmark", type="STRING"),
        Field(column="old_shelfmark", alias="old_shelfmarks", type="STRING[]"),
        Field(
            column="contents_of_record_without_shelfmark",
            alias="contents_of_record_without_shelfmark",
            type="STRING",
        ),
        Field(column="collection", alias="collection", type="STRING"),
        Field(
            column="case when is_hypothetical like 'Yes' then true else false end",
            alias="is_hypothetical",
            type="BOOLEAN",
        ),
        Field(
            column="collection_of_fragments",
            alias="collection_of_fragments",
            type="STRING",
        ),
        Field(column="described_at_URL", alias="urls", type="STRING[]"),
        Field(column="online_catalogue_URL", alias="catalogue_url", type="STRING"),
        Field(column="ARK", alias="ark", type="STRING"),
    ]

    _from = """FROM DocumentTable"""
