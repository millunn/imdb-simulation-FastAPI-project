from datetime import datetime
from uuid import uuid4

from sqlalchemy import INT, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base


class MovieRatingAndReview(Base):
    __tablename__ = "movies_rating_and_review"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    grade = Column(INT, nullable=False)
    comment = Column(String(200))
    comment_date = Column(
        String(50),
        default=datetime.strftime(datetime.now(), "%Y-%m-%d, %H:%M:%S"),
    )

    movie_id = Column(String(50), ForeignKey("movies.id"))
    movie = relationship("Movie", lazy="subquery")

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="subquery")
    __table_args__ = (UniqueConstraint("movie_id", "user_id", name="movie_user_uc"),)

    def __init__(self, grade, comment, movie_id, user_id):
        self.grade = grade
        self.comment = comment
        self.movie_id = movie_id
        self.user_id = user_id
