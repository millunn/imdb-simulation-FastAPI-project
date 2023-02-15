from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    PrimaryKeyConstraint,
    String,
)


class MovieAward(Base):
    __tablename__ = "movie_award"
    movie_id = Column(String(50), ForeignKey("movies.id"))
    movie = relationship("Movie", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"))
    award = relationship("Award", lazy="subquery")

    __table_args__ = (PrimaryKeyConstraint("movie_id", "award_id"),)

    def __init__(self, movie_id, award_id):
        self.movie_id = movie_id
        self.award_id = award_id
