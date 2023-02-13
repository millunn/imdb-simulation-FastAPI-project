from pydantic import UUID4, BaseModel


class GenreSchema(BaseModel):
    id: UUID4
    category: str
    description: str

    class Config:
        orm_mode = True


class GenreSchemaIn(BaseModel):
    category: str
    description: str

    class Config:
        orm_mode = True
