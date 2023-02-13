import datetime
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
    release_year = Column(Date)
    director = Column(String(50))
    writer = Column(String(50))
    producer = Column(String(50))
    synopsis = Column(String(180))

    language_id = Column(String(50), ForeignKey("languages.id"))
    language = relationship("Language", lazy="subquery")

    genre_id = Column(String(50), ForeignKey("genres.id"))
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
        language_id,
        genre_id,
    ):
        self.title = title
        self.plot = plot
        self.duration = datetime.strptime(duration, "%H:%M")
        self.release_year = datetime.strptime(release_year, "%Y-%m-%d")
        self.director = director
        self.writer = writer
        self.producer = producer
        self.synopsis = synopsis
        self.language_id = language_id
        self.genre_id = genre_id
