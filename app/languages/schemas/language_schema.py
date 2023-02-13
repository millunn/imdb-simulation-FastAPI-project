from pydantic import UUID4, BaseModel


class LanguageSchema(BaseModel):
    id: UUID4
    name: str
    abbreviation: str

    class Config:
        orm_mode = True


class LanguageSchemaIn(BaseModel):
    name: str
    abbreviation: str

    class Config:
        orm_mode = True
