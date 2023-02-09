from pydantic import UUID4, BaseModel


class AwardSchema(BaseModel):
    id: UUID4
    category: str
    subcategory: str

    class Config:
        orm_mode = True


class AwardSchemaIn(BaseModel):
    category: str
    subcategory: str

    class Config:
        orm_mode = True
