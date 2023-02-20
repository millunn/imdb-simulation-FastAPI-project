from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.movies.exceptions import MovieNotFoundException
from app.movies.exceptions import MovieIntegrityException

from app.movies.models import Movie
from app.ratings_and_reviews.models import MovieRatingAndReview


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
        language_name,
        genre_category,
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
                language_name,
                genre_category,
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

    def get_movie_by_title(self, title: str):
        movie = self.db.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided title: {title} not found.",
                code=400,
            )
        return movie

    def get_movie_by_language(self, language: str):
        movie = (
            self.db.query(Movie)
            .filter(Movie.language_name.ilike(f"%{language}%"))
            .all()
        )
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided language: {language} not found.",
                code=400,
            )
        return movie

    def get_movie_by_genre(self, genre: str):
        movie = (
            self.db.query(Movie).filter(Movie.genre_category.ilike(f"%{genre}%")).all()
        )
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided genre: {genre} not found.",
                code=400,
            )
        return movie

    def get_movie_by_release_year(self, release_year: str):
        movie = self.db.query(Movie).filter(Movie.release_year == release_year).all()
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided release_year: {release_year} not found.",
                code=400,
            )
        return movie

    def get_all_movies(self):
        movies = self.db.query(Movie).all()
        if (movies is None) or (movies == []):
            raise MovieNotFoundException(
                message=f"The list is empty!",
                code=400,
            )
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
        except IntegrityError as e:
            raise MovieIntegrityException(
                message=f"Cannot delete a parent row!",
                code=400,
            )
        except Exception as e:
            raise e

    def order_movies_by_title_decs(self):
        order_by_title_desc = self.db.query(Movie).order_by(Movie.title.desc()).all()
        return order_by_title_desc

    def order_movies_by_title_asc(self):
        order_by_title_asc = self.db.query(Movie).order_by(Movie.title.asc()).all()
        return order_by_title_asc

    def get_top_five_movies_by_ratings(self):
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .group_by(MovieRatingAndReview.movie_id)
            .order_by(desc("average_rating"))
            .limit(5)
            .values(
                MovieRatingAndReview.movie_id.label("movie_id"),
                func.avg(MovieRatingAndReview.grade).label("average_rating"),
            )
        )
        return movie_rating_and_review

    def get_top_five_most_rated_movies(self):
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .group_by(MovieRatingAndReview.movie_id)
            .order_by(desc("number_of_ratings"))
            .limit(5)
            .values(
                MovieRatingAndReview.movie_id.label("movie_id"),
                func.count(MovieRatingAndReview.grade).label("number_of_ratings"),
            )
        )
        return movie_rating_and_review
