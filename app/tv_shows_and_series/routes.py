from fastapi import APIRouter, Depends
from app.ratings_and_reviews.schemas import (
    MostRatedTVShowSchema,
    TopFiveTVShowSchema,
)
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
    MostAwardedTVShowsSchema,
)


from app.users.controller.user_auth_controller import JWTBearer

tv_show_router = APIRouter(tags=["tv_shows_and_series"], prefix="/api/tv_show")
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


@tv_show_router.get("/order-by-title/desc", response_model=list[TVShowSchema])
def order_tv_show_by_title_decs():
    return TVShowController.order_tv_show_by_title_decs()


@tv_show_router.get("/order-by-title/asc", response_model=list[TVShowSchema])
def order_tv_show_by_title_asc():
    return TVShowController.order_tv_show_by_title_asc()


@tv_show_router.get("/get-top-five-tv_shows", response_model=list[TopFiveTVShowSchema])
def get_top_five_tv_shows_by_ratings():
    return TVShowController.get_top_five_tv_shows_by_ratings()


@tv_show_router.get("/most-rated-tv_shows", response_model=list[MostRatedTVShowSchema])
def get_five_most_rated_tv_shows():
    return TVShowController.get_five_most_rated_tv_shows()


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


@tv_show_award_router.get(
    "/most-awarded-tv-shows", response_model=list[MostAwardedTVShowsSchema]
)
def get_top_five_most_awarded_tv_shows():
    return TVShowAwardController.get_top_five_most_awarded_tv_shows()
