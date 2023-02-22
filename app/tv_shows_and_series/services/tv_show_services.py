""" TVShow Services module """

from app.db.database import SessionLocal
from app.genres.exceptions import GenreNotFoundException
from app.genres.repository import GenreRepository
from app.languages.exceptions import LanguageNotFoundException
from app.languages.repository import LanguageRepository
from app.tv_shows_and_series.exceptions import (
    TVShowEpisodeDurationException,
    TVShowReleaseYearDigitException,
    TVShowReleaseYearLenghtException,
)
from app.tv_shows_and_series.repository import TVShowRepository


class TVShowServices:
    """TVShow model services"""

    @staticmethod
    def create_tv_show(
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
            if len(str(episode_duration)) > 4:
                raise TVShowEpisodeDurationException(
                    message="Episode duration minutes must be between 1 and 999!",
                    code=400,
                )
            if not release_year.isdigit():
                raise TVShowReleaseYearDigitException(
                    message="Release year not an integer!",
                    code=400,
                )
            if len(release_year) > 4:
                raise TVShowReleaseYearLenghtException(
                    message="Release year must have 4 digits!",
                    code=400,
                )
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                language = language_repository.get_language_by_name(language_name)
                if language is None:
                    raise LanguageNotFoundException(
                        message=f"Language with provided name: {language_name} not found.",
                        code=400,
                    )
                genre_repository = GenreRepository(db)
                genre = genre_repository.get_genre_by_category(genre_category)
                if genre is None:
                    raise GenreNotFoundException(
                        message=f"Genre with provided category: {genre_category} not found.",
                        code=400,
                    )
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.create_tv_show(
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
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_id(tv_show_id: str):
        """Get tv_show by id"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_id(tv_show_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_title(title: str):
        """Get tv_show by title"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_title(title)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_language(language: str):
        """Get tv_show by language"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_language(language)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_genre(genre: str):
        """Get tv_show by genre"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_genre(genre)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_release_year(release_year: str):
        """Get tv_show by release_year"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_release_year(release_year)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_tv_shows():
        """Get all tv_shows"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_all_tv_shows()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_tv_show_by_id(tv_show_id: str):
        """Delete tv_show by id"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.delete_tv_show_by_id(tv_show_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def order_tv_show_by_title_decs():
        """Order tv_show by title in a decsending order"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.order_tv_show_by_title_decs()
        except Exception as e:
            raise e from e

    @staticmethod
    def order_tv_show_by_title_asc():
        """Order tv_show by title in a acsending order"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.order_tv_show_by_title_asc()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_top_five_tv_shows_by_ratings():
        """Get top five tv_shows by ratings"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_top_five_tv_shows_by_ratings()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_five_most_rated_tv_shows():
        """Get five most rated tv_shows"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_five_most_rated_tv_shows()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_genre_statistics():
        """Get genre statistics"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_genre_statistics()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_language_statistics():
        """Get language statistics"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_language_statistics()
        except Exception as e:
            raise e from e
