""" Actor/Actress-Award-Movie Model module """

from uuid import uuid4
from sqlalchemy import Column, ForeignKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class ActorActressAwardMovie(Base):
    """Actor/Actress-Award-Movie model"""

    __tablename__ = "actor_actress_award_movie"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    actor_actress_id = Column(String(50), nullable=False)
    actor_actress = relationship(
        "ActorActress",
        lazy="subquery",
    )

    award_id = Column(String(50), nullable=False)
    award = relationship(
        "Award",
        lazy="subquery",
    )

    movie_id = Column(String(50), nullable=False)
    movie = relationship(
        "Movie",
        lazy="subquery",
    )

    __table_args__ = (
        ForeignKeyConstraint(["actor_actress_id"], ["actors_actresses.id"]),
        ForeignKeyConstraint(["award_id"], ["awards.id"]),
        ForeignKeyConstraint(["movie_id"], ["movies.id"]),
        UniqueConstraint(
            "actor_actress_id",
            "award_id",
            "movie_id",
            name="actor_actress_award_movie_uc",
        ),
    )

    def __init__(self, actor_actress_id, award_id, movie_id):
        self.actor_actress_id = actor_actress_id
        self.award_id = award_id
        self.movie_id = movie_id
