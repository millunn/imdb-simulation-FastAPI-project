from app.db.database import SessionLocal
from app.genres.exceptions import GenreNotFoundException
from app.genres.repository import GenreRepository
from app.languages.exceptions import LanguageNotFoundException
from app.languages.repository import LanguageRepository
from app.movies.exceptions import (
    MovieDurationException,
    MovieReleaseYearDigitException,
    MovieReleaseYearLenghtException,
)
from app.movies.repository import MovieRepository


class MovieServices:
    @staticmethod
    def create_movie(
        title,
        plot,
        duration,
        release_year,
        director,
        writer,
        producer,
        synopsis,
        language_name,
        genre_category,
    ):
        try:
            if len(str(duration)) > 4:
                raise MovieDurationException(
                    message=f"Duration minutes must be between 1 and 999!",
                    code=400,
                )
            if not release_year.isdigit():
                raise MovieReleaseYearDigitException(
                    message=f"Release year not an integer!",
                    code=400,
                )
            if len(release_year) > 4:
                raise MovieReleaseYearLenghtException(
                    message=f"Release year must have 4 digits!",
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
                movie_repository = MovieRepository(db)
                return movie_repository.create_movie(
                    title,
                    plot,
                    duration,
                    release_year,
                    director,
                    writer,
                    producer,
                    synopsis,
                    language_name,
                    genre_category,
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_id(movie_id: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_id(movie_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_title(title: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_title(title)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_language(language: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_language(language)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_release_year(release_year: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_release_year(release_year)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_movies():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_all_movies()
        except Exception as e:
            raise e

    @staticmethod
    def delete_movie_by_id(movie_id: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.delete_movie_by_id(movie_id)
        except Exception as e:
            raise e

    @staticmethod
    def order_movies_by_title_decs():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.order_movies_by_title_decs()
        except Exception as e:
            raise e

    @staticmethod
    def order_movies_by_title_asc():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.order_movies_by_title_asc()
        except Exception as e:
            raise e

    @staticmethod
    def get_top_five_movies_by_ratings():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_top_five_movies_by_ratings()
        except Exception as e:
            raise e

    @staticmethod
    def get_top_five_most_rated_movies():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_top_five_most_rated_movies()
        except Exception as e:
            raise e

    @staticmethod
    def get_genre_statistics():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_genre_statistics()
        except Exception as e:
            raise e

    @staticmethod
    def get_language_statistics():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_language_statistics()
        except Exception as e:
            raise e

    @staticmethod
    def order_movie_duration_by_release_year_desc():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.order_movie_duration_by_release_year_desc()
        except Exception as e:
            raise e
