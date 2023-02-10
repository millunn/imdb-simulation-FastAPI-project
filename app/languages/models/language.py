from enum import unique
from sqlalchemy import Column, String
from uuid import uuid4

from app.db import Base


class Language(Base):
    __tablename__ = "languages"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), unique=True)
    abbreviation = Column(String(4))

    def __init__(self, name: str, abbreviation: str):
        self.name = name
        self.abbreviation = abbreviation
