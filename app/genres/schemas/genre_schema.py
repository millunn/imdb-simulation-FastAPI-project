""" Genre Schema module """

from pydantic import UUID4, BaseModel


class GenreSchema(BaseModel):
    """Genre Schema for output"""

    id: UUID4
    category: str
    description: str

    class Config:
        orm_mode = True


class GenreSchemaIn(BaseModel):
    """Genre Schema for input"""

    category: str
    description: str

    class Config:
        orm_mode = True
