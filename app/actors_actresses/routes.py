from fastapi import APIRouter, Depends
from app.actors_actresses.controller import (
    ActorActressController,
    ActorActressAwardMovieController,
)
from app.actors_actresses.schemas import (
    ActorActressSchema,
    ActorActressSchemaIn,
    ActorActressAwardMovieSchema,
    ActorActressAwardMovieSchemaIn,
    AwardByActorActressSchemaOut,
    ActorActressByAwardSchemaOut,
    ActorActressByMovieSchemaOut,
    AwardByMovieSchemaOut,
)


from app.users.controller.user_auth_controller import JWTBearer

actor_actress_router = APIRouter(tags=["actors_actresses"], prefix="/api/actor_actress")
actor_actress_award_movie_router = APIRouter(
    tags=["actor_actress_award_movie"], prefix="/api/actor_actress_award_movie"
)


# superuser
@actor_actress_router.post(
    "/add-new-actor-actress",
    response_model=ActorActressSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_actor_actress(actor_actress: ActorActressSchemaIn):
    return ActorActressController.create_actor_actress(
        actor_actress.name,
        actor_actress.surname,
        actor_actress.gender,
        actor_actress.about,
    )


@actor_actress_router.get("/id", response_model=ActorActressSchema)
def get_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.get_actor_actress_by_id(actor_actress_id)


@actor_actress_router.get("/name", response_model=list[ActorActressSchema])
def get_actor_actress_by_name(name: str):
    return ActorActressController.get_actor_actress_by_name(name)


@actor_actress_router.get("/surname", response_model=ActorActressSchema)
def get_actor_actress_by_surname(surname: str):
    return ActorActressController.get_actor_actress_by_surname(surname)


@actor_actress_router.get(
    "/get-all-actor-actresses", response_model=list[ActorActressSchema]
)
def get_all_actor_actresss():
    return ActorActressController.get_all_actor_actresss()


# superuser
@actor_actress_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.delete_actor_actress_by_id(actor_actress_id)


# superuser
@actor_actress_award_movie_router.post(
    "/add-new-actor-actress-award-movie",
    response_model=ActorActressAwardMovieSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_actor_actress_award_movie(
    actor_actress_award_movie: ActorActressAwardMovieSchemaIn,
):
    return ActorActressAwardMovieController.create_actor_actress_award_movie(
        actor_actress_award_movie.actor_actress_id,
        actor_actress_award_movie.award_id,
        actor_actress_award_movie.movie_id,
    )


@actor_actress_award_movie_router.get(
    "/actor-actress-id", response_model=list[AwardByActorActressSchemaOut]
)
def get_award_by_actor_actress_id(actor_actress_id: str):
    return ActorActressAwardMovieController.get_award_by_actor_actress_id(
        actor_actress_id
    )


@actor_actress_award_movie_router.get(
    "/award/movie-id", response_model=list[AwardByMovieSchemaOut]
)
def get_award_by_movie_id(movie_id: str):
    return ActorActressAwardMovieController.get_award_by_movie_id(movie_id)


@actor_actress_award_movie_router.get(
    "/award-id/", response_model=list[ActorActressByAwardSchemaOut]
)
def get_actor_actress_by_award_id(award_id: str):
    return ActorActressAwardMovieController.get_actor_actress_by_award_id(award_id)


@actor_actress_award_movie_router.get(
    "/actor-actress/movie-id", response_model=list[ActorActressByMovieSchemaOut]
)
def get_actor_actress_by_movie_id(movie_id: str):
    return ActorActressAwardMovieController.get_actor_actress_by_movie_id(movie_id)


@actor_actress_award_movie_router.get(
    "/get-all-actor_actresses-with-all-awards-all-movies",
    response_model=list[ActorActressAwardMovieSchema],
)
def get_all_actor_actress_with_all_awards_all_movies():
    return (
        ActorActressAwardMovieController.get_all_actor_actress_with_all_awards_all_movies()
    )
