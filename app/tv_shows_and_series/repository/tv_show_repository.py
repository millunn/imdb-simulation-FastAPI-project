""" TVShow Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.ratings_and_reviews.models import TVShowRatingAndReview
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.models import TVShow


class TVShowRepository:
    """TVShow model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_tv_show(
        self,
        title,
        plot,
        release_year,
        creator,
        seasons,
        episodes,
        episode_duration,
        language_name,
        genre_category,
    ):
        """Create new tv_show"""
        try:
            tv_show = TVShow(
                title,
                plot,
                release_year,
                creator,
                seasons,
                episodes,
                episode_duration,
                language_name,
                genre_category,
            )
            self.db.add(tv_show)
            self.db.commit()
            self.db.refresh(tv_show)
            return tv_show
        except IntegrityError as e:
            raise e from e

    def get_tv_show_by_id(self, tv_show_id: str):
        """Get tv_show by id"""
        tv_show = self.db.query(TVShow).filter(TVShow.id == tv_show_id).first()
        if tv_show is None:
            raise TVShowNotFoundException(
                message=f"Tv show with provided id: {tv_show_id} not found.",
                code=400,
            )
        return tv_show

    def get_tv_show_by_title(self, title: str):
        """Get tv_show by title"""
        tv_show = self.db.query(TVShow).filter(TVShow.title.ilike(f"%{title}%")).all()
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided title: {title} not found.",
                code=400,
            )
        return tv_show

    def get_tv_show_by_language(self, language: str):
        """Get tv_show by language"""
        tv_show = (
            self.db.query(TVShow)
            .filter(TVShow.language_name.ilike(f"%{language}%"))
            .all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided language: {language} not found.",
                code=400,
            )
        return tv_show

    def get_tv_show_by_genre(self, genre: str):
        """Get tv_show by genre"""
        tv_show = (
            self.db.query(TVShow)
            .filter(TVShow.genre_category.ilike(f"%{genre}%"))
            .all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided genre: {genre} not found.",
                code=400,
            )
        return tv_show

    def get_tv_show_by_release_year(self, release_year: str):
        """Get tv_show by release_year"""
        tv_show = (
            self.db.query(TVShow).filter(TVShow.release_year == release_year).all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided release_year: {release_year} not found.",
                code=400,
            )
        return tv_show

    def get_all_tv_shows(self):
        """Get all tv_shows"""
        tv_shows = self.db.query(TVShow).all()
        if (tv_shows is None) or (tv_shows == []):
            raise TVShowNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return tv_shows

    def delete_tv_show_by_id(self, tv_show_id: str):
        """Delete tv_show by id"""
        try:
            tv_show = self.db.query(TVShow).filter(TVShow.id == tv_show_id).first()
            if tv_show is None:
                raise TVShowNotFoundException(
                    message=f"Tv show with provided id: {tv_show_id} not found.",
                    code=400,
                )
            self.db.delete(tv_show)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e

    def order_tv_show_by_title_decs(self):
        """Order tv_show by title in a decsending order"""
        order_by_title_desc = self.db.query(TVShow).order_by(TVShow.title.desc()).all()
        return order_by_title_desc

    def order_tv_show_by_title_asc(self):
        """Order tv_show by title in a acsending order"""
        order_by_title_asc = self.db.query(TVShow).order_by(TVShow.title.asc()).all()
        return order_by_title_asc

    def get_top_five_tv_shows_by_ratings(self):
        """Get top five tv_shows by ratings"""
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .group_by(TVShowRatingAndReview.tv_show_id)
            .order_by(desc("average_rating"))
            .limit(5)
            .values(
                TVShowRatingAndReview.tv_show_id.label("tv_show_id"),
                func.avg(TVShowRatingAndReview.grade).label("average_rating"),
            )
        )
        return tv_show_rating_and_review

    def get_five_most_rated_tv_shows(self):
        """Get five most rated tv_shows"""
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .group_by(TVShowRatingAndReview.tv_show_id)
            .order_by(desc("number_of_ratings"))
            .limit(5)
            .values(
                TVShowRatingAndReview.tv_show_id.label("tv_show_id"),
                func.count(TVShowRatingAndReview.grade).label("number_of_ratings"),
            )
        )
        return tv_show_rating_and_review

    def get_genre_statistics(self):
        """Get genre statistics"""
        genre_statistics = (
            self.db.query(TVShow)
            .group_by(TVShow.genre_category)
            .order_by(desc("category_count"))
            .values(
                TVShow.genre_category.label("genre_category"),
                func.count(TVShow.genre_category).label("category_count"),
            )
        )
        return genre_statistics

    def get_language_statistics(self):
        """Get language statistics"""
        language_statistics = (
            self.db.query(TVShow)
            .group_by(TVShow.language_name)
            .order_by(desc("language_count"))
            .values(
                TVShow.language_name.label("language_name"),
                func.count(TVShow.language_name).label("language_count"),
            )
        )
        return language_statistics
