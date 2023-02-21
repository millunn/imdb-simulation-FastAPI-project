from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.genres.exceptions import GenreNotFoundException
from app.languages.exceptions import LanguageNotFoundException
from app.movies.exceptions import (
    MovieNotFoundException,
    MovieIntegrityException,
    MovieReleaseYearDigitException,
    MovieReleaseYearLenghtException,
)

from app.movies.services import MovieServices


class MovieController:
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
        except MovieReleaseYearDigitException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except MovieReleaseYearLenghtException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Movie with provided data already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_id(movie_id: str):
        try:
            movie = MovieServices.get_movie_by_id(movie_id)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_title(title: str):
        try:
            movie = MovieServices.get_movie_by_title(title)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_language(language: str):
        try:
            movie = MovieServices.get_movie_by_language(language)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_genre(genre: str):
        try:
            movie = MovieServices.get_movie_by_genre(genre)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_release_year(release_year: str):
        try:
            movie = MovieServices.get_movie_by_release_year(release_year)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_movies():
        try:
            movies = MovieServices.get_all_movies()
            return movies
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_movie_by_id(movie_id: str):
        try:
            MovieServices.delete_movie_by_id(movie_id)
            return Response(content=f"Movie with provided id - {movie_id} is deleted")
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except MovieIntegrityException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def order_movies_by_title_decs():
        try:
            order_by_title_desc = MovieServices.order_movies_by_title_decs()
            return order_by_title_desc
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def order_movies_by_title_asc():
        try:
            order_by_title_asc = MovieServices.order_movies_by_title_asc()
            return order_by_title_asc
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_top_five_movies_by_ratings():
        try:
            movies = MovieServices.get_top_five_movies_by_ratings()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_top_five_most_rated_movies():
        try:
            movies = MovieServices.get_top_five_most_rated_movies()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_genre_statistics():
        try:
            movies = MovieServices.get_genre_statistics()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_language_statistics():
        try:
            movies = MovieServices.get_language_statistics()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # @staticmethod
    # def order_movie_duration_by_release_year_desc():
    #     try:
    #         movies = MovieServices.order_movie_duration_by_release_year_desc()
    #         return movies
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=str(e))
