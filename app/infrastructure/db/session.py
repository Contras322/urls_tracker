from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@asynccontextmanager
async def get_context(session_maker: "async_sessionmaker") -> AsyncIterator["AsyncSession"]:
    """Контекстный менеджер для создания сессии."""
    async with session_maker.begin() as session:
        yield session
