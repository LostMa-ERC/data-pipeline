from ._base import Base, Field


class Language(Base):
    fields = [
        Field(column="trm_ID", alias="id", type="INT64"),
        Field(column="trm_Label", alias="name", type="STRING"),
        Field(column="trm_Description", alias="description", type="STRING"),
        Field(column="trm_Code", alias="code", type="STRING"),
        Field(column="trm_SemanticReferenceURL", alias="url", type="STRING"),
    ]

    _from = "FROM trm WHERE trm_ParentTermID = 9469"
