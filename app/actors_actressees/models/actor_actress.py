from sqlalchemy import Column, String, UniqueConstraint
from uuid import uuid4

from app.db import Base


class ActorActress(Base):
    __tablename__ = "actors_actresses"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    gender = Column(String(1), nullable=False)
    about = Column(String(180), nullable=False)

    __table_args__ = (
        UniqueConstraint("name", "surname", "about", name="name_surname_about_uc"),
    )

    def __init__(self, name: str, surname: str, gender: str, about: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.about = about
