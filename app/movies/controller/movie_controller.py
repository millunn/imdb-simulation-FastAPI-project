from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.movies.exceptions import MovieNotFoundException

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
        language_id,
        genre_id,
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
                language_id,
                genre_id,
            )
            return movie
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
    def get_all_movies():
        try:
            movies = MovieServices.get_all_movies()
            return movies
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
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
