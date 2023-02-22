from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class MovieAward(Base):
    __tablename__ = "movie_award"
    movie_id = Column(String(50), ForeignKey("movies.id"), nullable=False)
    movie = relationship("Movie", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"), nullable=False)
    award = relationship("Award", lazy="subquery")

    __table_args__ = (PrimaryKeyConstraint("movie_id", "award_id"),)

    def __init__(self, movie_id, award_id):
        self.movie_id = movie_id
        self.award_id = award_id
