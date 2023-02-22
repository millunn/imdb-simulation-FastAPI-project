import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.actors_actresses.routes import (
    actor_actress_award_movie_router,
    actor_actress_award_tv_show_router,
    actor_actress_router,
)
from app.awards.routes import award_router
from app.db.database import Base, engine
from app.genres.routes import genre_router
from app.languages.routes import language_router
from app.movies.routes import (
    movie_actor_actress_router,
    movie_award_router,
    movie_router,
)
from app.ratings_and_reviews.routes import (
    movie_rating_and_review_router,
    tv_show_rating_and_review_router,
)
from app.tv_shows_and_series.routes import (
    tv_show_actor_actress_router,
    tv_show_award_router,
    tv_show_router,
)
from app.users.routes import user_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(award_router)
    app.include_router(genre_router)
    app.include_router(language_router)
    app.include_router(actor_actress_router)
    app.include_router(actor_actress_award_movie_router)
    app.include_router(actor_actress_award_tv_show_router)
    app.include_router(movie_router)
    app.include_router(movie_actor_actress_router)
    app.include_router(movie_award_router)
    app.include_router(tv_show_router)
    app.include_router(tv_show_actor_actress_router)
    app.include_router(tv_show_award_router)
    app.include_router(movie_rating_and_review_router)
    app.include_router(tv_show_rating_and_review_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
