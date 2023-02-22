from uuid import uuid4

from sqlalchemy import INT, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class Movie(Base):
    """Movie model"""

    __tablename__ = "movies"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    title = Column(String(50), nullable=False)
    plot = Column(String(100), nullable=False)
    duration = Column(INT, nullable=False)
    release_year = Column(String(4), nullable=False)
    director = Column(String(50), nullable=False)
    writer = Column(String(50), nullable=False)
    producer = Column(String(50), nullable=False)
    synopsis = Column(String(180), nullable=False)

    language_name = Column(String(30), ForeignKey("languages.name"), nullable=False)
    language = relationship("Language", lazy="subquery")

    genre_category = Column(String(30), ForeignKey("genres.category"), nullable=False)
    genre = relationship("Genre", lazy="subquery")

    __table_args__ = (
        UniqueConstraint("title", "release_year", name="title_release_year_uc"),
    )

    def __init__(
        self,
        title,
        plot,
        duration,
        release_year,
        director,
        writer,
        producer,
        synopsis,
        language_name,
        genre_category,
    ):
        self.title = title
        self.plot = plot
        self.duration = duration
        self.release_year = release_year
        self.director = director
        self.writer = writer
        self.producer = producer
        self.synopsis = synopsis
        self.language_name = language_name
        self.genre_category = genre_category
