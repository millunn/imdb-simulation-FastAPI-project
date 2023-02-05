import uvicorn
from fastapi import FastAPI

from db.database import engine, Base


Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    return app


app = init_app()

if __name__ == "__main__":
    uvicorn.run(app)
