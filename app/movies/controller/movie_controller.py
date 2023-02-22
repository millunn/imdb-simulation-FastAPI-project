""" Movie Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.genres.exceptions import GenreNotFoundException
from app.languages.exceptions import LanguageNotFoundException
from app.movies.exceptions import (
    MovieDurationException,
    MovieIntegrityException,
    MovieNotFoundException,
    MovieReleaseYearDigitException,
    MovieReleaseYearLenghtException,
)
from app.movies.services import MovieServices


class MovieController:
    """Movie model controller"""

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
        """Create new movie"""
        try:
            movie = MovieServices.create_movie(
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
            return movie
        except MovieDurationException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except MovieReleaseYearDigitException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except MovieReleaseYearLenghtException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Movie with provided data already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_id(movie_id: str):
        """Get movie by id"""
        try:
            movie = MovieServices.get_movie_by_id(movie_id)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_title(title: str):
        """Get movie by title"""
        try:
            movie = MovieServices.get_movie_by_title(title)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_language(language: str):
        """Get movie by language"""
        try:
            movie = MovieServices.get_movie_by_language(language)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_genre(genre: str):
        """Get movie by genre"""
        try:
            movie = MovieServices.get_movie_by_genre(genre)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_release_year(release_year: str):
        """Get movie by release_year"""
        try:
            movie = MovieServices.get_movie_by_release_year(release_year)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_movies():
        """Get all movies"""
        try:
            movies = MovieServices.get_all_movies()
            return movies
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_movie_by_id(movie_id: str):
        """Delete movie by id"""
        try:
            MovieServices.delete_movie_by_id(movie_id)
            return Response(content=f"Movie with provided id - {movie_id} is deleted")
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except MovieIntegrityException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_movies_by_title_decs():
        """Order movies by title in decsending order"""
        try:
            order_by_title_desc = MovieServices.order_movies_by_title_decs()
            return order_by_title_desc
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_movies_by_title_asc():
        """Order movies by title in acsending order"""
        try:
            order_by_title_asc = MovieServices.order_movies_by_title_asc()
            return order_by_title_asc
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_movies_by_ratings():
        """Get top five movies by ratings"""
        try:
            movies = MovieServices.get_top_five_movies_by_ratings()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_most_rated_movies():
        """Get five most rated movies"""
        try:
            movies = MovieServices.get_top_five_most_rated_movies()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_genre_statistics():
        """Get genre statistics"""
        try:
            movies = MovieServices.get_genre_statistics()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_language_statistics():
        """Get language statistics"""
        try:
            movies = MovieServices.get_language_statistics()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_movie_duration_by_release_year_desc():
        """Order movie duration by release year in decsending order"""
        try:
            movies = MovieServices.order_movie_duration_by_release_year_desc()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
