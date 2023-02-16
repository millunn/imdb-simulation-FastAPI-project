import uuid
from fastapi import APIRouter, Depends
from pydantic import UUID4

from app.movies.controller import (
    MovieController,
    MovieActorActressController,
    MovieAwardController,
)

from app.movies.schemas import (
    MovieSchema,
    MovieSchemaSchemaIn,
    MovieActorActressSchema,
    MovieActorActressSchemaIn,
    MovieByActorActressSchemaOut,
    ActorActressByMovieSchemaOut,
    AwardByMovieSchemaOut,
    MovieByAwardSchemaOut,
    MovieAwardSchema,
    MovieAwardSchemaIn,
)


from app.users.controller.user_auth_controller import JWTBearer

movie_router = APIRouter(tags=["movies"], prefix="/api/movie")
movie_actor_actress_router = APIRouter(
    tags=["movie_actor_actress"], prefix="/api/movie_actor_actress"
)
movie_award_router = APIRouter(tags=["movie_award"], prefix="/api/movie_award")


# superuser
@movie_router.post(
    "/add-new-movie",
    response_model=MovieSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_movie(movie: MovieSchemaSchemaIn):
    return MovieController.create_movie(
        movie.title,
        movie.plot,
        movie.duration,
        movie.release_year,
        movie.director,
        movie.writer,
        movie.producer,
        movie.synopsis,
        movie.language_name,
        movie.genre_category,
    )


@movie_router.get("/id", response_model=MovieSchema)
def get_movie_by_id(movie_id: str):
    return MovieController.get_movie_by_id(movie_id)


@movie_router.get("/title", response_model=list[MovieSchema])
def get_movie_by_title(title: str):
    return MovieController.get_movie_by_title(title)


@movie_router.get("/language", response_model=list[MovieSchema])
def get_movie_by_language(language: str):
    return MovieController.get_movie_by_language(language)


@movie_router.get("/genre", response_model=list[MovieSchema])
def get_movie_by_genre(genre: str):
    return MovieController.get_movie_by_genre(genre)


@movie_router.get("/release_year", response_model=list[MovieSchema])
def get_movie_by_release_year(release_year: str):
    return MovieController.get_movie_by_release_year(release_year)


@movie_router.get("/get-all-movies", response_model=list[MovieSchema])
def get_all_movies():
    return MovieController.get_all_movies()


# superuser
@movie_router.delete(
    "/",
)  # dependencies=[Depends(JWTBearer("super_user"))])
def delete_movie_by_id(movie_id: str):
    return MovieController.delete_movie_by_id(movie_id)


# superuser
@movie_actor_actress_router.post(
    "/add-new-movie-actor-actress",
    response_model=MovieActorActressSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_movie_actor_actress(
    movie_actor_actress_award: MovieActorActressSchemaIn,
):
    return MovieActorActressController.create_movie_actor_actress(
        movie_actor_actress_award.movie_id, movie_actor_actress_award.actor_actress_id
    )


@movie_actor_actress_router.get(
    "/actor-actress-id", response_model=list[MovieByActorActressSchemaOut]
)
def get_movie_by_actor_actress_id(actor_actress_id: str):
    return MovieActorActressController.get_movie_by_actor_actress_id(actor_actress_id)


@movie_actor_actress_router.get(
    "/actor-actress/movie-id", response_model=list[ActorActressByMovieSchemaOut]
)
def get_actor_actress_by_movie_id(movie_id: str):
    return MovieActorActressController.get_actor_actress_by_movie_id(movie_id)


@movie_actor_actress_router.get(
    "/get-all-movies-with-all-actor-actresses",
    response_model=list[MovieActorActressSchema],
)
def get_all_movies_with_all_actors_actresses():
    return MovieActorActressController.get_all_movies_with_all_actors_actresses()


# superuser
@movie_award_router.post(
    "/add-new-movie-award",
    response_model=MovieAwardSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_movie_award(
    movie_award_award: MovieAwardSchemaIn,
):
    return MovieAwardController.create_movie_award(
        movie_award_award.movie_id, movie_award_award.award_id
    )


@movie_award_router.get("/award-id", response_model=list[MovieByAwardSchemaOut])
def get_movie_by_award_id(award_id: str):
    return MovieAwardController.get_movie_by_award_id(award_id)


@movie_award_router.get("/award/movie-id", response_model=list[AwardByMovieSchemaOut])
def get_award_by_movie_id(movie_id: str):
    return MovieAwardController.get_award_by_movie_id(movie_id)


@movie_award_router.get(
    "/get-all-movies-with-all-awards",
    response_model=list[MovieActorActressSchema],
)
def get_all_movies_with_all_awards():
    return MovieAwardController.get_all_movies_with_all_awards()
