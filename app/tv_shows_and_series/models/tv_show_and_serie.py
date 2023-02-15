from sqlite3 import Date
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import INT, Column, ForeignKey, String, Time, Date
from uuid import uuid4


class TVShowAndSerie(Base):
    __tablename__ = "tv_shows_and_series"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    title = Column(String(50), unique=True, nullable=False)
    plot = Column(String(100), nullable=False)
    release_year = Column(Date, nullable=False)
    creator = Column(String(50), nullable=False)
    seasons = Column(INT, nullable=False)
    episodes = Column(INT, nullable=False)
    episode_duration = Column(Time, nullable=False)

    language_id = Column(String(50), ForeignKey("languages.id"))
    language = relationship("Language", lazy="subquery")

    genre_id = Column(String(50), ForeignKey("genres.id"))
    genre = relationship("Genre", lazy="subquery")

    def __init__(
        self,
        title,
        plot,
        release_year,
        creator,
        seasons,
        episodes,
        episode_duration,
        language_id,
        genre_id,
    ):
        self.title = title
        self.plot = plot
        self.release_year = release_year
        self.creator = creator
        self.seasons = seasons
        self.episodes = episodes
        self.episode_duration = episode_duration
        self.language_id = language_id
        self.genre_id = genre_id
