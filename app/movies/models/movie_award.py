from uuid import uuid4
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class MovieAward(Base):
    """MovieAward model"""

    __tablename__ = "movie_award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    movie_id = Column(String(50), ForeignKey("movies.id"), nullable=False)
    movie = relationship("Movie", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"), nullable=False)
    award = relationship("Award", lazy="subquery")

    __table_args__ = (UniqueConstraint("movie_id", "award_id", name="movie_award_uc"),)

    def __init__(self, movie_id, award_id):
        self.movie_id = movie_id
        self.award_id = award_id
