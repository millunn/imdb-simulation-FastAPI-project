from uuid import uuid4
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class TVShowActorActress(Base):
    __tablename__ = "tv_show_actor_actress"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    tv_show_id = Column(
        String(50), ForeignKey("tv_shows_and_series.id"), nullable=False
    )
    tv_show = relationship("TVShow", lazy="subquery")

    actor_actress_id = Column(
        String(50), ForeignKey("actors_actresses.id"), nullable=False
    )
    actor_actress = relationship("ActorActress", lazy="subquery")

    __table_args__ = (
        UniqueConstraint(
            "tv_show_id", "actor_actress_id", name="tv_show_actor_actress_uc"
        ),
    )

    def __init__(self, tv_show_id, actor_actress_id):
        self.tv_show_id = tv_show_id
        self.actor_actress_id = actor_actress_id
