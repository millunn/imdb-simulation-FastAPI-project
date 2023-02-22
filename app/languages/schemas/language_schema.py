""" Language Schema module """

from pydantic import UUID4, BaseModel


class LanguageSchema(BaseModel):
    """Language Schema for output"""

    id: UUID4
    name: str
    abbreviation: str

    class Config:
        orm_mode = True


class LanguageSchemaIn(BaseModel):
    """Language Schema for input"""

    name: str
    abbreviation: str

    class Config:
        orm_mode = True
