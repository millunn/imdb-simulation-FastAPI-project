""" Award Schema module """

from pydantic import UUID4, BaseModel


class AwardSchema(BaseModel):
    """Award Schema for output"""

    id: UUID4
    category: str
    subcategory: str

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    """Award Schema for input"""

    category: str
    subcategory: str

    class Config:
        orm_mode = True
