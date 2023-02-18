from fastapi import APIRouter

from app.ratings_and_reviews.controller import (
    MovieRatingAndReviewController,
    TVShowRatingAndReviewController,
)
from app.ratings_and_reviews.schemas import (
    MovieRatingAndReviewSchema,
    MovieRatingAndReviewSchemaIn,
    MovieRatingAndReviewBySchemaOut,
    MovieRatingAndReviewSchemaUpdateComment,
)
from app.ratings_and_reviews.schemas import (
    TVShowRatingAndReviewSchema,
    TVShowRatingAndReviewSchemaIn,
    TVShowRatingAndReviewBySchemaOut,
    TVShowRatingAndReviewSchemaUpdateComment,
)


movie_rating_and_review_router = APIRouter(
    tags=["movies_ratings_and_reviews"], prefix="/api/movies_ratings_and_reviews"
)
tv_show_rating_and_review_router = APIRouter(
    tags=["tv_shows_ratings_and_reviews"], prefix="/api/tv_shows_ratings_and_reviews"
)


# superuser
@movie_rating_and_review_router.post(
    "/add-new-movie-rating-and-review",
    response_model=MovieRatingAndReviewSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_movie_rating_and_review(movie: MovieRatingAndReviewSchemaIn):
    return MovieRatingAndReviewController.create_movie_rating_and_review(
        movie.grade,
        movie.comment,
        movie.movie_id,
        movie.user_id,
    )


@movie_rating_and_review_router.get(
    "/movie-rating-and-review-id", response_model=MovieRatingAndReviewSchema
)  # dependencies=[Depends(JWTBearer("super_user"))])
def get_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
    return MovieRatingAndReviewController.get_movie_rating_and_review_by_id(
        movie_rating_and_review_id
    )


@movie_rating_and_review_router.get(
    "/grade", response_model=list[MovieRatingAndReviewBySchemaOut]
)
def get_movie_rating_and_review_by_grade(grade: str):
    return MovieRatingAndReviewController.get_movie_rating_and_review_by_grade(grade)


@movie_rating_and_review_router.get(
    "/movie-id", response_model=list[MovieRatingAndReviewBySchemaOut]
)
def get_movie_rating_and_review_by_movie_id(movie_id: str):
    return MovieRatingAndReviewController.get_movie_rating_and_review_by_movie_id(
        movie_id
    )


@movie_rating_and_review_router.get(
    "/user-id", response_model=list[MovieRatingAndReviewSchema]
)  # dependencies=[Depends(JWTBearer("super_user"))])
def get_movie_rating_and_review_by_user_id(user_id: str):
    return MovieRatingAndReviewController.get_movie_rating_and_review_by_user_id(
        user_id
    )


@movie_rating_and_review_router.get(
    "/get-all-movies", response_model=list[MovieRatingAndReviewBySchemaOut]
)
def get_all_movies_ratings_and_reviews():
    return MovieRatingAndReviewController.get_all_movies_ratings_and_reviews()


# superuser
@movie_rating_and_review_router.delete(
    "/",
)  # dependencies=[Depends(JWTBearer("super_user"))])
def delete_movie_rating_and_review_by_id(movie_id: str):
    return MovieRatingAndReviewController.delete_movie_rating_and_review_by_id(movie_id)


@movie_rating_and_review_router.put(
    "/comment-update/comment", response_model=MovieRatingAndReviewSchema
)
def update_movie_rating_and_review_comment(
    movie_rating_and_review_id: str,
    update_data: MovieRatingAndReviewSchemaUpdateComment,
):
    return MovieRatingAndReviewController.update_movie_rating_and_review_comment(
        movie_rating_and_review_id, update_data.comment
    )


# superuser
@tv_show_rating_and_review_router.post(
    "/add-new-tv-show-rating-and-review",
    response_model=TVShowRatingAndReviewSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show_rating_and_review(tv_show: TVShowRatingAndReviewSchemaIn):
    return TVShowRatingAndReviewController.create_tv_show_rating_and_review(
        tv_show.grade,
        tv_show.comment,
        tv_show.tv_show_id,
        tv_show.user_id,
    )


@tv_show_rating_and_review_router.get(
    "/tv-show-rating-and-review-id", response_model=TVShowRatingAndReviewSchema
)  # dependencies=[Depends(JWTBearer("super_user"))])
def get_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
    return TVShowRatingAndReviewController.get_tv_show_rating_and_review_by_id(
        tv_show_rating_and_review_id
    )


@tv_show_rating_and_review_router.get(
    "/grade", response_model=list[TVShowRatingAndReviewBySchemaOut]
)
def get_tv_show_rating_and_review_by_grade(grade: str):
    return TVShowRatingAndReviewController.get_tv_show_rating_and_review_by_grade(grade)


@tv_show_rating_and_review_router.get(
    "/tv-show-id", response_model=list[TVShowRatingAndReviewBySchemaOut]
)
def get_tv_show_rating_and_review_by_tv_show_id(tv_show_id: str):
    return TVShowRatingAndReviewController.get_tv_show_rating_and_review_by_tv_show_id(
        tv_show_id
    )


@tv_show_rating_and_review_router.get(
    "/user-id", response_model=list[TVShowRatingAndReviewSchema]
)  # dependencies=[Depends(JWTBearer("super_user"))])
def get_tv_show_rating_and_review_by_user_id(user_id: str):
    return TVShowRatingAndReviewController.get_tv_show_rating_and_review_by_user_id(
        user_id
    )


@tv_show_rating_and_review_router.get(
    "/get-all-tv-shows", response_model=list[TVShowRatingAndReviewBySchemaOut]
)
def get_all_tv_shows_ratings_and_reviews():
    return TVShowRatingAndReviewController.get_all_tv_shows_ratings_and_reviews()


# superuser
@tv_show_rating_and_review_router.delete(
    "/",
)  # dependencies=[Depends(JWTBearer("super_user"))])
def delete_tv_show_rating_and_review_by_id(tv_show_id: str):
    return TVShowRatingAndReviewController.delete_tv_show_rating_and_review_by_id(
        tv_show_id
    )


@tv_show_rating_and_review_router.put(
    "/comment-update/comment", response_model=TVShowRatingAndReviewSchema
)
def update_tv_show_rating_and_review_comment(
    tv_show_rating_and_review_id: str,
    update_data: TVShowRatingAndReviewSchemaUpdateComment,
):
    return TVShowRatingAndReviewController.update_tv_show_rating_and_review_comment(
        tv_show_rating_and_review_id, update_data.comment
    )
