from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.movies.exceptions import MovieNotFoundException

from app.movies.models import Movie


class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_movie(
        self,
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
            movie = Movie(
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
            self.db.add(movie)
            self.db.commit()
            self.db.refresh(movie)
            return movie
        except IntegrityError as e:
            raise e

    def get_movie_by_id(self, movie_id: str):
        movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        if movie is None:
            raise MovieNotFoundException(
                message=f"Movie with provided id: {movie_id} not found.",
                code=400,
            )
        return movie

    # lista
    def get_movie_by_title(self, title: str):
        movie = self.db.query(Movie).filter(Movie.title == title).all()
        if movie is None:
            raise MovieNotFoundException(
                message=f"Movie with provided title: {title} not found.",
                code=400,
            )
        return movie

    def get_all_movies(self):
        movies = self.db.query(Movie).all()
        return movies

    ##superuser
    def delete_movie_by_id(self, movie_id: str):
        try:
            movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
            if movie is None:
                raise MovieNotFoundException(
                    message=f"Movie with provided id: {movie_id} not found.",
                    code=400,
                )
            self.db.delete(movie)
            self.db.commit()
            return True
        except Exception as e:
            raise e
