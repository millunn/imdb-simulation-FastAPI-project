from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.awards.exceptions import AwardNotFoundException
from app.movies.exceptions import MovieNotFoundException
from app.movies.services import MovieAwardServices


class MovieAwardController:
    @staticmethod
    def create_movie_award(movie_id, award_id):
        try:
            movie_award = MovieAwardServices.create_movie_award(movie_id, award_id)
            return movie_award

        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )

        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_by_award_id(award_id: str):
        try:
            movie = MovieAwardServices.get_movie_by_award_id(award_id)
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_movie_id(movie_id: str):
        try:
            award = MovieAwardServices.get_award_by_movie_id(movie_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_movies_with_all_awards():
        try:
            movie_award_repository = MovieAwardServices.get_all_movies_with_all_awards()
            return movie_award_repository
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_top_five_most_awarded_movies():
        try:
            movies = MovieAwardServices.get_top_five_most_awarded_movies()
            return movies
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
