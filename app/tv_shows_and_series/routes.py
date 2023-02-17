from fastapi import APIRouter, Depends
from app.tv_shows_and_series.controller import (
    TvShowController,
    TvShowActorActressController,
    TvShowAwardController,
)


from app.tv_shows_and_series.schemas import (
    TvShowSchema,
    TvShowSchemaSchemaIn,
    TvShowActorActressSchema,
    TvShowActorActressSchemaIn,
    TvShowByActorActressSchemaOut,
    ActorActressByTvShowSchemaOut,
    AwardByTvShowSchemaOut,
    TvShowByAwardSchemaOut,
    TvShowAwardSchema,
    TvShowAwardSchemaIn,
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
    response_model=TvShowSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show(tv_show: TvShowSchemaSchemaIn):
    return TvShowController.create_tv_show(
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


@tv_show_router.get("/id", response_model=TvShowSchema)
def get_tv_show_by_id(tv_show_id: str):
    return TvShowController.get_tv_show_by_id(tv_show_id)


@tv_show_router.get("/title", response_model=list[TvShowSchema])
def get_tv_show_by_title(title: str):
    return TvShowController.get_tv_show_by_title(title)


@tv_show_router.get("/language", response_model=list[TvShowSchema])
def get_tv_show_by_language(language: str):
    return TvShowController.get_tv_show_by_language(language)


@tv_show_router.get("/genre", response_model=list[TvShowSchema])
def get_tv_show_by_genre(genre: str):
    return TvShowController.get_tv_show_by_genre(genre)


@tv_show_router.get("/release_year", response_model=list[TvShowSchema])
def get_tv_show_by_release_year(release_year: str):
    return TvShowController.get_tv_show_by_release_year(release_year)


@tv_show_router.get("/get-all-tv_shows", response_model=list[TvShowSchema])
def get_all_tv_shows():
    return TvShowController.get_all_tv_shows()


# superuser
@tv_show_router.delete(
    "/",
)  # dependencies=[Depends(JWTBearer("super_user"))])
def delete_tv_show_by_id(tv_show_id: str):
    return TvShowController.delete_tv_show_by_id(tv_show_id)


# superuser
@tv_show_actor_actress_router.post(
    "/add-new-tv_show-actor-actress",
    response_model=TvShowActorActressSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show_actor_actress(
    tv_show_actor_actress_award: TvShowActorActressSchemaIn,
):
    return TvShowActorActressController.create_tv_show_actor_actress(
        tv_show_actor_actress_award.tv_show_id,
        tv_show_actor_actress_award.actor_actress_id,
    )


@tv_show_actor_actress_router.get(
    "/actor-actress-id", response_model=list[TvShowByActorActressSchemaOut]
)
def get_tv_show_by_actor_actress_id(actor_actress_id: str):
    return TvShowActorActressController.get_tv_show_by_actor_actress_id(
        actor_actress_id
    )


@tv_show_actor_actress_router.get(
    "/actor-actress/tv_show-id", response_model=list[ActorActressByTvShowSchemaOut]
)
def get_actor_actress_by_tv_show_id(tv_show_id: str):
    return TvShowActorActressController.get_actor_actress_by_tv_show_id(tv_show_id)


@tv_show_actor_actress_router.get(
    "/get-all-tv_shows-with-all-actor-actresses",
    response_model=list[TvShowActorActressSchema],
)
def get_all_tv_shows_with_all_actors_actresses():
    return TvShowActorActressController.get_all_tv_shows_with_all_actors_actresses()


# superuser
@tv_show_award_router.post(
    "/add-new-tv_show-award",
    response_model=TvShowAwardSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_tv_show_award(
    tv_show_award_award: TvShowAwardSchemaIn,
):
    return TvShowAwardController.create_tv_show_award(
        tv_show_award_award.tv_show_id, tv_show_award_award.award_id
    )


@tv_show_award_router.get("/award-id", response_model=list[TvShowByAwardSchemaOut])
def get_tv_show_by_award_id(award_id: str):
    return TvShowAwardController.get_tv_show_by_award_id(award_id)


@tv_show_award_router.get(
    "/award/tv_show-id", response_model=list[AwardByTvShowSchemaOut]
)
def get_award_by_tv_show_id(tv_show_id: str):
    return TvShowAwardController.get_award_by_tv_show_id(tv_show_id)


@tv_show_award_router.get(
    "/get-all-tv_shows-with-all-awards",
    response_model=list[TvShowAwardSchemaIn],
)
def get_all_tv_shows_with_all_awards():
    return TvShowAwardController.get_all_tv_shows_with_all_awards()
