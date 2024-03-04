from fastapi import FastAPI

from url_shortener.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    app.celery_app = create_celery()

    from url_shortener.url_shorts.shorts import router

    app.include_router(router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app
