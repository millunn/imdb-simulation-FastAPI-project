from xmlrpc.client import Boolean
from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __init__(
        self, name, surname, email, password, is_active=True, is_superuser=False
    ):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser
