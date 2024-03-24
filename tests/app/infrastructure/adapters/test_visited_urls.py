from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest

from app.domain.entities.visited_url import VisitedUrl
from app.infrastructure.adapters.visited_urls import VisitedUrlsAdapter
from tests.app.infrastructure.adapters.conftest import session_ctx_factory

# pylint: disable=protected-access, redefined-outer-name, unnecessary-dunder-call

FAKE_DTTM = datetime.now()
NOTE = VisitedUrl(link="https://www.test.ru", visit_dttm=FAKE_DTTM)
DOMAIN = "test"


@pytest.fixture
def adapter(session: AsyncMock) -> VisitedUrlsAdapter:
    """Фикстура объекта VisitedUrlsAdapter."""
    adapter = VisitedUrlsAdapter(session_ctx_factory(session))
    adapter._visited_urls = MagicMock()  # type: ignore
    adapter._visited_urls.visit_dttm = FAKE_DTTM

    return adapter


class _ModulePatch:
    """Класс с патчами текущего модуля."""

    _PATH = "app.infrastructure.adapters.visited_urls"

    SELECT = f"{_PATH}.select"
    INSERT = f"{_PATH}.insert"
    AND = f"{_PATH}.and_"


class TestVisitedUrlsAdapter:
    """Тестирование методов адаптера VisitedUrlsAdapter."""

    @patch(_ModulePatch.INSERT)
    async def test__add(
        self, insert: MagicMock, session: AsyncMock, adapter: VisitedUrlsAdapter
    ) -> None:
        """Тест метода add() на успешность."""

        await adapter.add(NOTE)

        assert session.mock_calls == [call.execute(insert().values())]

    @patch(_ModulePatch.SELECT)
    async def test__get_domains(
        self, select: MagicMock, session: AsyncMock, adapter: VisitedUrlsAdapter
    ) -> None:
        """Тест метода get_domains() на успешность."""
        execute_result = MagicMock()
        execute_result.scalars.return_value.all.return_value = [DOMAIN]
        session.execute.return_value = execute_result

        assert await adapter.get_domains(FAKE_DTTM, FAKE_DTTM) == [DOMAIN]

        assert session.mock_calls == [
            call.execute(select().distinct().where().where().where()),
            call.execute().scalars(),
            call.execute().scalars().all(),
        ]

    @patch(_ModulePatch.SELECT)
    async def test__get_domains__without_params(
        self, select: MagicMock, session: AsyncMock, adapter: VisitedUrlsAdapter
    ) -> None:
        """Тест метода get_domains() на успешность. Кейс с отсутствием параметров."""
        execute_result = MagicMock()
        execute_result.scalars.return_value.all.return_value = [DOMAIN]
        session.execute.return_value = execute_result

        assert await adapter.get_domains() == [DOMAIN]

        assert session.mock_calls == [
            call.execute(select().distinct().where()),
            call.execute().scalars(),
            call.execute().scalars().all(),
        ]
