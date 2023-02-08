from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint


class ActorActressAward(Base):
    __tablename__ = "actor_actress_award"
    actor_actress_id = Column(String(50), ForeignKey("actors_actresses.id"))
    actor_actress = relationship("ActorActress", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"))
    award = relationship("Award", lazy="subquery")

    __table_args__ = (
        UniqueConstraint("actor_actress_id", "award_id", name="actor_actress_award_uc"),
    )

    def __init__(self, actor_actress_id, award_id):
        self.actor_actress_id = actor_actress_id
        self.award_id = award_id
