from sqlalchemy import Column, String
from uuid import uuid4

from app.db import Base


class Award(Base):
    __tablename__ = "awards"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    category = Column(String(50))
    subcategory = Column(String(50))

    def __init__(self, category: str, subcategory: str):
        self.category = category
        self.subcategory = subcategory
