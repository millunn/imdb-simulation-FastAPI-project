""" Movie Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.movies.exceptions import MovieIntegrityException, MovieNotFoundException
from app.movies.models import Movie
from app.ratings_and_reviews.models import MovieRatingAndReview


class MovieRepository:
    """Movie model repository"""

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
        """Create new movie"""
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
            raise e from e

    def get_movie_by_id(self, movie_id: str):
        """Get movie by id"""
        movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        if movie is None:
            raise MovieNotFoundException(
                message=f"Movie with provided id: {movie_id} not found.",
                code=400,
            )
        return movie

    def get_movie_by_title(self, title: str):
        """Get movie by title"""
        movie = self.db.query(Movie).filter(Movie.title.ilike(f"%{title}%")).all()
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided title: {title} not found.",
                code=400,
            )
        return movie

    def get_movie_by_language(self, language: str):
        """Get movie by language"""
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
        """Get movie by genre"""
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
        """Get movie by release_year"""
        movie = self.db.query(Movie).filter(Movie.release_year == release_year).all()
        if (movie is None) or (movie == []):
            raise MovieNotFoundException(
                message=f"Movie with provided release_year: {release_year} not found.",
                code=400,
            )
        return movie

    def get_all_movies(self):
        """Get all movies"""
        movies = self.db.query(Movie).all()
        if (movies is None) or (movies == []):
            raise MovieNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return movies

    def delete_movie_by_id(self, movie_id: str):
        """Delete movie by id"""
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
                message="Cannot delete a parent row!",
                code=400,
            ) from e
        except Exception as e:
            raise e from e

    def order_movies_by_title_decs(self):
        """Order movies by title in decsending order"""
        order_by_title_desc = self.db.query(Movie).order_by(Movie.title.desc()).all()
        return order_by_title_desc

    def order_movies_by_title_asc(self):
        """Order movies by title in acsending order"""
        order_by_title_asc = self.db.query(Movie).order_by(Movie.title.asc()).all()
        return order_by_title_asc

    def get_top_five_movies_by_ratings(self):
        """Get top five movies by ratings"""
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
        """Get five most rated movies"""
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

    def get_genre_statistics(self):
        """Get genre statistics"""
        genre_statistics = (
            self.db.query(Movie)
            .group_by(Movie.genre_category)
            .order_by(desc("category_count"))
            .values(
                Movie.genre_category.label("genre_category"),
                func.count(Movie.genre_category).label("category_count"),
            )
        )
        return genre_statistics

    def get_language_statistics(self):
        """Get language statistics"""
        language_statistics = (
            self.db.query(Movie)
            .group_by(Movie.language_name)
            .order_by(desc("language_count"))
            .values(
                Movie.language_name.label("language_name"),
                func.count(Movie.language_name).label("language_count"),
            )
        )
        return language_statistics

    def order_movie_duration_by_release_year_desc(self):
        """Order movie duration by release year in decsending order"""
        movie_duration_by_release_year = (
            self.db.query(Movie)
            .group_by(Movie.release_year)
            .order_by(desc("average_duration"))
            .values(
                Movie.release_year.label("release_year"),
                func.avg(Movie.duration).label("average_duration"),
            )
        )
        return movie_duration_by_release_year
