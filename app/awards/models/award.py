from uuid import uuid4

from sqlalchemy import Column, String, UniqueConstraint

from app.db import Base


class Award(Base):
    """Award model"""

    __tablename__ = "awards"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    category = Column(String(50), nullable=False)
    subcategory = Column(String(50), nullable=False)

    __table_args__ = (
        UniqueConstraint("category", "subcategory", name="_category_subcategory_uc"),
    )

    def __init__(self, category: str, subcategory: str):
        self.category = category
        self.subcategory = subcategory
