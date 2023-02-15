from sqlalchemy import Column, String
from uuid import uuid4

from app.db import Base


class Genre(Base):
    __tablename__ = "genres"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    category = Column(String(50), unique=True, nullable=False)
    description = Column(String(500), nullable=False)

    def __init__(self, category: str, description: str):
        self.category = category
        self.description = description
