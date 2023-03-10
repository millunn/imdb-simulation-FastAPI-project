""" Actor/Actress-Award-TvShow Model module """

from uuid import uuid4
from sqlalchemy import (
    Column,
    ForeignKey,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class ActorActressAwardTvShow(Base):
    """Actor/Actress-Award-TvShow model"""

    __tablename__ = "actor_actress_award_tv_show"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    actor_actress_id = Column(
        String(50), ForeignKey("actors_actresses.id"), nullable=False
    )
    actor_actress = relationship(
        "ActorActress",
        lazy="subquery",
    )

    award_id = Column(String(50), ForeignKey("awards.id"), nullable=False)
    award = relationship(
        "Award",
        lazy="subquery",
    )

    tv_show_id = Column(
        String(50), ForeignKey("tv_shows_and_series.id"), nullable=False
    )
    tv_show = relationship(
        "TVShow",
        lazy="subquery",
    )

    __table_args__ = (
        UniqueConstraint(
            "actor_actress_id",
            "award_id",
            "tv_show_id",
            name="actor_actress_award_tv_show_uc",
        ),
    )

    def __init__(self, actor_actress_id, award_id, tv_show_id):
        self.actor_actress_id = actor_actress_id
        self.award_id = award_id
        self.tv_show_id = tv_show_id
