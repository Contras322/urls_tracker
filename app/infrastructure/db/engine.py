from typing import TYPE_CHECKING

from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine

    from app.settings.db import DBSettings


def get_async(settings: "DBSettings") -> "AsyncEngine":
    """Получить асинхронный `engine` для работы с базой данных."""
    engine = create_async_engine(url=settings.url)

    @event.listens_for(engine.sync_engine, "connect", insert=True)
    def set_search_path(dbapi_conn, _conn_record):
        existing_autocommit = dbapi_conn.autocommit
        dbapi_conn.autocommit = True

        cursor = dbapi_conn.cursor()
        cursor.execute(f"SET search_path TO {settings.app_schema}")
        cursor.close()

        dbapi_conn.autocommit = existing_autocommit

    return engine
