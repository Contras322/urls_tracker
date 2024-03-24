from http import HTTPStatus

from fastapi import APIRouter, status

from app.container import APP_CONTAINER
from app.presentation.api import responses
from app.presentation.api.base.routers.schemas import VersionSchema

SYSTEM_TAG = "system"
SYSTEM_PREFIX = f"/{SYSTEM_TAG}"

router = APIRouter(prefix=SYSTEM_PREFIX, tags=[SYSTEM_TAG])


@router.get("/liveness", status_code=status.HTTP_204_NO_CONTENT)
async def liveness() -> None:
    """Проверка доступности сервиса."""
    return None


@router.get(
    "/readiness", status_code=status.HTTP_204_NO_CONTENT, responses=responses.SERVICE_UNAVAILABLE
)
async def readiness() -> None:
    """Проверка готовности сервиса."""
    return None


@router.get("/version", status_code=HTTPStatus.OK)
async def version() -> VersionSchema:
    """Получить текущую версию приложения."""
    return VersionSchema(version=APP_CONTAINER.api_settings().version)
