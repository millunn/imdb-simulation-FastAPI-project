import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base
from app.users.routes import user_router
from app.awards.routes import award_router
from app.genres.routes import genre_router
from app.languages.routes import language_router
from app.actors_actressees.routes import (
    actor_actress_router,
    actor_actress_award_router,
)
from app.movies.routes import movie_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(award_router)
    app.include_router(genre_router)
    app.include_router(language_router)
    app.include_router(actor_actress_router)
    app.include_router(actor_actress_award_router)
    app.include_router(movie_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
