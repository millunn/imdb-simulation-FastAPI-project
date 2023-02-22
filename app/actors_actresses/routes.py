""" Routes module """

from fastapi import APIRouter, Depends

from app.actors_actresses.controller import (
    ActorActressAwardMovieController,
    ActorActressAwardTvShowController,
    ActorActressController,
)
from app.actors_actresses.schemas import (
    ActorActressAwardMovieSchema,
    ActorActressAwardMovieSchemaIn,
    ActorActressAwardTVShowSchema,
    ActorActressAwardTVShowSchemaIn,
    ActorActressByAwardSchemaOut,
    ActorActressByMovieSchemaOut,
    ActorActressByTVShowSchemaOut,
    ActorActressGenderStatisticsSchema,
    ActorActressSchema,
    ActorActressSchemaIn,
    ActorActressSchemaUpdateAboutSection,
    AwardByActorActressSchemaOut,
    AwardByMovieSchemaOut,
    AwardByTVShowSchemaOut,
    MostAwardedMovieActorsActressesSchema,
    MostAwardedTVShowActorsActressesSchema,
)
from app.users.controller.user_auth_controller import JWTBearer

actor_actress_router = APIRouter(tags=["actors_actresses"], prefix="/api/actor_actress")
actor_actress_award_movie_router = APIRouter(
    tags=["actor_actress_award_movie"], prefix="/api/actor_actress_award_movie"
)
actor_actress_award_tv_show_router = APIRouter(
    tags=["actor_actress_award_tv_show"], prefix="/api/actor_actress_award_tv_show"
)


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


@actor_actress_router.get("/gender", response_model=list[ActorActressSchema])
def get_actor_actress_by_gender(gender: str):
    return ActorActressController.get_actor_actress_by_gender(gender)


@actor_actress_router.get("/surname", response_model=list[ActorActressSchema])
def get_actor_actress_by_surname(surname: str):
    return ActorActressController.get_actor_actress_by_surname(surname)


@actor_actress_router.get(
    "/get-all-actors-actresses", response_model=list[ActorActressSchema]
)
def get_all_actors_actresses():
    return ActorActressController.get_all_actors_actresses()


@actor_actress_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.delete_actor_actress_by_id(actor_actress_id)


@actor_actress_router.get(
    "/order-by-name/desc", response_model=list[ActorActressSchema]
)
def order_actor_actress_by_name_decs():
    return ActorActressController.order_actor_actress_by_name_decs()


@actor_actress_router.get("/order-by-name/asc", response_model=list[ActorActressSchema])
def order_actor_actress_by_name_asc():
    return ActorActressController.order_actor_actress_by_name_asc()


@actor_actress_router.get(
    "/gender/statistics", response_model=list[ActorActressGenderStatisticsSchema]
)
def get_gender_statistics():
    return ActorActressController.get_gender_statistics()


@actor_actress_router.put("/about-update/about", response_model=ActorActressSchema)
def update_actor_actress_about_section(
    actor_actress_id: str,
    update_data: ActorActressSchemaUpdateAboutSection,
):
    return ActorActressController.update_actor_actress_about_section(
        actor_actress_id, update_data.about
    )


@actor_actress_award_movie_router.post(
    "/add-new-actor-actress-award-movie",
    response_model=ActorActressAwardMovieSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
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
    "/get-all-actors-actresses-with-all-awards-all-movies",
    response_model=list[ActorActressAwardMovieSchema],
)
def get_all_actors_actresses_with_all_awards_all_movies():
    return (
        ActorActressAwardMovieController.get_all_actors_actresses_with_all_awards_all_movies()
    )


@actor_actress_award_movie_router.get(
    "/most-rated-movie-actors-actresses",
    response_model=list[MostAwardedMovieActorsActressesSchema],
)
def get_top_five_most_awarded_movie_actors_actresses():
    return (
        ActorActressAwardMovieController.get_top_five_most_awarded_movie_actors_actresses()
    )


@actor_actress_award_movie_router.delete(
    "/", dependencies=[Depends(JWTBearer("super_user"))]
)
def delete_actor_actress_award_movie_by_id(actor_actress_award_movie_id: str):
    return ActorActressAwardMovieController.delete_actor_actress_award_movie_by_id(
        actor_actress_award_movie_id
    )


@actor_actress_award_tv_show_router.post(
    "/add-new-actor-actress-award-tv-show",
    response_model=ActorActressAwardTVShowSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_actor_actress_award_tv_show(
    actor_actress_award_tv_show: ActorActressAwardTVShowSchemaIn,
):
    return ActorActressAwardTvShowController.create_actor_actress_award_tv_show(
        actor_actress_award_tv_show.actor_actress_id,
        actor_actress_award_tv_show.award_id,
        actor_actress_award_tv_show.tv_show_id,
    )


@actor_actress_award_tv_show_router.get(
    "/actor-actress-id", response_model=list[AwardByActorActressSchemaOut]
)
def get_award_by_actor_actress_id(actor_actress_id: str):
    return ActorActressAwardTvShowController.get_award_by_actor_actress_id(
        actor_actress_id
    )


@actor_actress_award_tv_show_router.get(
    "/award/tv-show-id", response_model=list[AwardByTVShowSchemaOut]
)
def get_award_by_tv_show_id(tv_show_id: str):
    return ActorActressAwardTvShowController.get_award_by_tv_show_id(tv_show_id)


@actor_actress_award_tv_show_router.get(
    "/award-id/", response_model=list[ActorActressByAwardSchemaOut]
)
def get_actor_actress_by_award_id(award_id: str):
    return ActorActressAwardTvShowController.get_actor_actress_by_award_id(award_id)


@actor_actress_award_tv_show_router.get(
    "/actor-actress/tv-show-id", response_model=list[ActorActressByTVShowSchemaOut]
)
def get_actor_actress_by_tv_show_id(tv_show_id: str):
    return ActorActressAwardTvShowController.get_actor_actress_by_tv_show_id(tv_show_id)


@actor_actress_award_tv_show_router.get(
    "/get-all-actors-actresses-with-all-awards-all-tv-shows",
    response_model=list[ActorActressAwardTVShowSchema],
)
def get_all_actors_actresses_with_all_awards_all_tv_shows():
    return (
        ActorActressAwardTvShowController.get_all_actors_actresses_with_all_awards_all_tv_shows()
    )


@actor_actress_award_tv_show_router.get(
    "/most-rated-tv-show-actors-actresses",
    response_model=list[MostAwardedTVShowActorsActressesSchema],
)
def get_top_five_most_awarded_tv_show_actors_actresses():
    return (
        ActorActressAwardTvShowController.get_top_five_most_awarded_tv_show_actors_actresses()
    )


@actor_actress_award_tv_show_router.delete(
    "/", dependencies=[Depends(JWTBearer("super_user"))]
)
def delete_actor_actress_award_tv_show_by_id(actor_actress_award_tv_show_id: str):
    return ActorActressAwardTvShowController.delete_actor_actress_award_tv_show_by_id(
        actor_actress_award_tv_show_id
    )
