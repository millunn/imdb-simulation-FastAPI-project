from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Language(Base):
    """Language model"""

    __tablename__ = "languages"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), unique=True, nullable=False)
    abbreviation = Column(String(4), unique=True, nullable=False)

    def __init__(self, name: str, abbreviation: str):
        self.name = name
        self.abbreviation = abbreviation
