import pytest
from fastapi.testclient import TestClient

from app.presentation.api.v1.factory import create_app

# pylint: disable=redefined-outer-name


@pytest.fixture()
def app_api():
    """Фикстура с приложением FastAPI."""
    app = create_app(title="test_app", version="9.9.9")

    return app


@pytest.fixture()
def client(app_api):
    """Синхронный тестовый клиент для приложений на FastAPI."""
    with TestClient(app_api) as client:
        yield client
