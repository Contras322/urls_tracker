from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Callable, Object, Singleton
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.infrastructure.adapters.visited_urls import VisitedUrlsAdapter
from app.infrastructure.db import engine, session
from app.settings.api import ApiEnvSettings, ApiSettings
from app.settings.db import DBSettings
from app.settings.server import ServerSettings
from utils.base_dir import BASE_DIR
from utils.pyproject import PyProjectData

if TYPE_CHECKING:
    from logging import Logger

    from sqlalchemy.ext.asyncio import AsyncEngine


_PYPROJECT_FILE = BASE_DIR / "pyproject.toml"


class AppContainer(DeclarativeContainer):
    """Контейнер зависимостей приложения."""

    _api_env_settings: Singleton["ApiEnvSettings"] = Singleton(ApiEnvSettings)
    _pyproject: Singleton[PyProjectData] = Singleton(PyProjectData.get_data, _PYPROJECT_FILE)

    # Настройки с постфиксом `settings` для валидации перед запуском компонент.
    api_settings: Singleton["ApiSettings"] = Singleton(
        ApiSettings, _api_env_settings.provided, _pyproject.provided
    )
    db_settings: Singleton["DBSettings"] = Singleton(DBSettings)
    server_settings: Singleton["ServerSettings"] = Singleton(ServerSettings)

    logger: Object["Logger"] = Object(logger)  # type: ignore

    engine: Singleton["AsyncEngine"] = Singleton(engine.get_async, settings=db_settings.provided)
    session_maker: Singleton["async_sessionmaker"] = Singleton(
        async_sessionmaker, bind=engine.provided
    )
    session_ctx: Callable[AbstractAsyncContextManager["AsyncSession"]] = Callable(
        session.get_context, session_maker=session_maker.provided
    )

    visited_urls_adapter: Singleton["VisitedUrlsAdapter"] = Singleton(
        VisitedUrlsAdapter, session_ctx.provider
    )


APP_CONTAINER = AppContainer()
