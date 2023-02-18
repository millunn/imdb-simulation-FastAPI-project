from fastapi import APIRouter, Depends
from app.tv_shows_and_series.controller import (
    TVShowController,
    TVShowActorActressController,
    TVShowAwardController,
)


from app.tv_shows_and_series.schemas import (
    TVShowSchema,
    TVShowSchemaSchemaIn,
    TVShowActorActressSchema,
    TVShowActorActressSchemaIn,
    TVShowByActorActressSchemaOut,
    ActorActressByTVShowSchemaOut,
    AwardByTVShowSchemaOut,
    TVShowByAwardSchemaOut,
    TVShowAwardSchema,
    TVShowAwardSchemaIn,
)


from app.users.controller.user_auth_controller import JWTBearer

tv_show_router = APIRouter(tags=["tv_shows"], prefix="/api/tv_show")
tv_show_actor_actress_router = APIRouter(
    tags=["tv_show_actor_actress"], prefix="/api/tv_show_actor_actress"
)
tv_show_award_router = APIRouter(tags=["tv_show_award"], prefix="/api/tv_show_award")


# superuser
@tv_show_router.post(
    "/add-new-tv_show",
    response_model=TVShowSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show(tv_show: TVShowSchemaSchemaIn):
    return TVShowController.create_tv_show(
        tv_show.title,
        tv_show.plot,
        tv_show.release_year,
        tv_show.creator,
        tv_show.seasons,
        tv_show.episodes,
        tv_show.episode_duration,
        tv_show.language_name,
        tv_show.genre_category,
    )


@tv_show_router.get("/id", response_model=TVShowSchema)
def get_tv_show_by_id(tv_show_id: str):
    return TVShowController.get_tv_show_by_id(tv_show_id)


@tv_show_router.get("/title", response_model=list[TVShowSchema])
def get_tv_show_by_title(title: str):
    return TVShowController.get_tv_show_by_title(title)


@tv_show_router.get("/language", response_model=list[TVShowSchema])
def get_tv_show_by_language(language: str):
    return TVShowController.get_tv_show_by_language(language)


@tv_show_router.get("/genre", response_model=list[TVShowSchema])
def get_tv_show_by_genre(genre: str):
    return TVShowController.get_tv_show_by_genre(genre)


@tv_show_router.get("/release_year", response_model=list[TVShowSchema])
def get_tv_show_by_release_year(release_year: str):
    return TVShowController.get_tv_show_by_release_year(release_year)


@tv_show_router.get("/get-all-tv_shows", response_model=list[TVShowSchema])
def get_all_tv_shows():
    return TVShowController.get_all_tv_shows()


# superuser
@tv_show_router.delete(
    "/",
)  # dependencies=[Depends(JWTBearer("super_user"))])
def delete_tv_show_by_id(tv_show_id: str):
    return TVShowController.delete_tv_show_by_id(tv_show_id)


# superuser
@tv_show_actor_actress_router.post(
    "/add-new-tv_show-actor-actress",
    response_model=TVShowActorActressSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show_actor_actress(
    tv_show_actor_actress_award: TVShowActorActressSchemaIn,
):
    return TVShowActorActressController.create_tv_show_actor_actress(
        tv_show_actor_actress_award.tv_show_id,
        tv_show_actor_actress_award.actor_actress_id,
    )


@tv_show_actor_actress_router.get(
    "/actor-actress-id", response_model=list[TVShowByActorActressSchemaOut]
)
def get_tv_show_by_actor_actress_id(actor_actress_id: str):
    return TVShowActorActressController.get_tv_show_by_actor_actress_id(
        actor_actress_id
    )


@tv_show_actor_actress_router.get(
    "/actor-actress/tv_show-id", response_model=list[ActorActressByTVShowSchemaOut]
)
def get_actor_actress_by_tv_show_id(tv_show_id: str):
    return TVShowActorActressController.get_actor_actress_by_tv_show_id(tv_show_id)


@tv_show_actor_actress_router.get(
    "/get-all-tv_shows-with-all-actor-actresses",
    response_model=list[TVShowActorActressSchema],
)
def get_all_tv_shows_with_all_actors_actresses():
    return TVShowActorActressController.get_all_tv_shows_with_all_actors_actresses()


# superuser
@tv_show_award_router.post(
    "/add-new-tv_show-award",
    response_model=TVShowAwardSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show_award(
    tv_show_award_award: TVShowAwardSchemaIn,
):
    return TVShowAwardController.create_tv_show_award(
        tv_show_award_award.tv_show_id, tv_show_award_award.award_id
    )


@tv_show_award_router.get("/award-id", response_model=list[TVShowByAwardSchemaOut])
def get_tv_show_by_award_id(award_id: str):
    return TVShowAwardController.get_tv_show_by_award_id(award_id)


@tv_show_award_router.get(
    "/award/tv_show-id", response_model=list[AwardByTVShowSchemaOut]
)
def get_award_by_tv_show_id(tv_show_id: str):
    return TVShowAwardController.get_award_by_tv_show_id(tv_show_id)


@tv_show_award_router.get(
    "/get-all-tv_shows-with-all-awards",
    response_model=list[TVShowAwardSchemaIn],
)
def get_all_tv_shows_with_all_awards():
    return TVShowAwardController.get_all_tv_shows_with_all_awards()