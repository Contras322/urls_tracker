from fastapi import FastAPI

from app.presentation.api import responses
from app.presentation.api.v1 import handlers
from app.presentation.api.v1.routers import visited_urls


def create_app(title: str, version: str) -> FastAPI:
    """Создать приложение FastAPI для текущего роута."""
    api_v1 = FastAPI(
        title=title,
        version=version,
        docs_url="/",
        redoc_url=None,
        responses=responses.INTERNAL_SERVER_ERROR,
    )

    # Добавление обработчиков исключений
    handlers.add_all(api_v1)

    # Добавление роутеров
    api_v1.include_router(visited_urls.router)

    return api_v1
