from fastapi import FastAPI
from src.containers.containers import Container
from src.router.endpoints import router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(router)
    return app


app = create_app()
