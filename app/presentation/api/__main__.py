from fastapi import FastAPI

from app.container import APP_CONTAINER
from app.presentation.api import handlers, responses
from app.presentation.api.base.routers import system
from app.presentation.api.v1 import factory as v1


def create_app():
    """Создать приложение FastAPI."""

    settings = APP_CONTAINER.api_settings()
    app = FastAPI(
        title=settings.title,
        version=settings.version,
        docs_url="/",
        redoc_url=None,
        responses=responses.INTERNAL_SERVER_ERROR,
    )

    # Подключение системного роутера
    app.include_router(system.router)
    handlers.add_all(app)

    # Подключение приложений.
    _mount_app(app, v1.create_app(settings.title, settings.version), "/api/v1")

    return app


def _mount_app(app: "FastAPI", sub_app: "FastAPI", sub_app_prefix: str) -> None:
    """Примонтировать приложение."""
    handlers.add_all(sub_app)
    app.mount(sub_app_prefix, sub_app)
