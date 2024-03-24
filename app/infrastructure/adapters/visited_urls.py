from collections.abc import Callable
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, ClassVar

from sqlalchemy import insert, select

from app.domain.entities.visited_url import VisitedUrl
from app.infrastructure.models.visited_urls import VisitedUrlsModel

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class VisitedUrlsAdapter:
    """Адаптер для работы с таблицей visited_urls."""

    _session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    _visited_urls: ClassVar = VisitedUrlsModel

    async def add(self, note: "VisitedUrl") -> None:
        """Сохранить запись о посещении ресурса."""
        insert_query = insert(self._visited_urls).values(
            {
                self._visited_urls.link: note.link,
                self._visited_urls.domain: note.domain,
                self._visited_urls.visit_dttm: note.visit_dttm,
            }
        )

        async with self._session_factory() as session:
            await session.execute(insert_query)

    async def get_domains(
        self, from_dttm: datetime | None = None, to_dttm: datetime | None = None
    ) -> list[str]:
        """Получить уникальные домейны, которые посетил пользователь в заданный промежуток."""
        select_query = (
            select(self._visited_urls.domain).distinct().where(self._visited_urls.domain != "")
        )

        if from_dttm:
            select_query = select_query.where(self._visited_urls.visit_dttm > from_dttm)

        if to_dttm:
            select_query = select_query.where(self._visited_urls.visit_dttm < to_dttm)

        async with self._session_factory() as session:
            domains = (await session.execute(select_query)).scalars().all()

        return list(domains)
