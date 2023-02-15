from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, String, Date, Time
from uuid import uuid4


class Movie(Base):
    __tablename__ = "movies"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    title = Column(String(50), unique=True)
    plot = Column(String(100))
    duration = Column(Time)
    release_year = Column(String(4))
    director = Column(String(50))
    writer = Column(String(50))
    producer = Column(String(50))
    synopsis = Column(String(180))

    language_name = Column(String(30), ForeignKey("languages.name"))
    language = relationship("Language", lazy="subquery")

    genre_category = Column(String(30), ForeignKey("genres.category"))
    genre = relationship("Genre", lazy="subquery")

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
        self.duration = datetime.strptime(duration, "%H:%M")
        self.release_year = release_year
        self.director = director
        self.writer = writer
        self.producer = producer
        self.synopsis = synopsis
        self.language_name = language_name
        self.genre_category = genre_category
