from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import freezegun
from fastapi import status

from app.container import APP_CONTAINER
from app.domain.entities.visited_url import VisitedUrl

API_PATH = ""
LINK = "https://www.test.ru"
DOMAIN = "www.test.ru"
FROM_ = 1711145626
TO = 1711145626


@freezegun.freeze_time()
def test__post_visited_links(client):
    """Тест метода POST /visited_links."""
    adapter = MagicMock(add=AsyncMock())
    visit_dttm = datetime.now()

    with APP_CONTAINER.visited_urls_adapter.override(adapter):
        response = client.post(f"{API_PATH}/visited_links", json={"links": [LINK]})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": status.HTTP_200_OK}
    adapter.add.assert_called_once_with(VisitedUrl(link=LINK, visit_dttm=visit_dttm))


def test__get_visited_domains(client):
    """Тест метода GET /visited_domains."""
    adapter = MagicMock(get_domains=AsyncMock(return_value=[DOMAIN]))

    with APP_CONTAINER.visited_urls_adapter.override(adapter):
        response = client.get(f"{API_PATH}/visited_domains", params={"from": FROM_, "to": TO})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"domains": [DOMAIN], "status": status.HTTP_200_OK}
    adapter.get_domains.assert_called_once_with(
        datetime.fromtimestamp(FROM_), datetime.fromtimestamp(TO)
    )


def test__get_visited_domains__without_params(client):
    """Тест метода GET /visited_domains без query параметров."""
    adapter = MagicMock(get_domains=AsyncMock(return_value=[DOMAIN]))

    with APP_CONTAINER.visited_urls_adapter.override(adapter):
        response = client.get(f"{API_PATH}/visited_domains")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"domains": [DOMAIN], "status": status.HTTP_200_OK}
    adapter.get_domains.assert_called_once_with(None, None)
