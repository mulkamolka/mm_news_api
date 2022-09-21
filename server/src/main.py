import logging

from src.containers.containers import Container
from src.router.endpoints import router
from fastapi import FastAPI

logger = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()

    app = FastAPI()
    app.include_router(router=router)

    return app


app = create_app()


# @app.on_event("startup")
# async def startup_event():
#     logger.info("Starting up...")
#     init_db(app)


# @app.on_event("shutdown")
# async def shutdown_event():
#     logger.info("Shutting down...")
