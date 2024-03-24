from datetime import datetime

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from app.container import APP_CONTAINER
from app.domain.entities.visited_url import VisitedUrl
from app.presentation.api.v1.schemas.visited_urls import VisitedUrlsSchema

TAG = ""
PREFIX = ""

router = APIRouter(prefix=PREFIX, tags=[TAG])


@router.post("/visited_links", summary="Обновить список посещенных ресурсов")
async def post_visited_links(data: VisitedUrlsSchema) -> JSONResponse:
    """POST запрос на добавление списка посещенных ресурсов."""
    visited_adapter = APP_CONTAINER.visited_urls_adapter()
    logger = APP_CONTAINER.logger()
    visit_dttm = datetime.now()

    for link in data.links:
        logger.info(f"Trying to save new visited link '{link}'...")
        await visited_adapter.add(VisitedUrl(link=link, visit_dttm=visit_dttm))

    return JSONResponse(content={"status": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)


@router.get("/visited_domains", summary="Получить список уникальных доменов посещенных ресурсов")
async def get_visited_domains(
    from_: int | None = Query(None, description="Начало отрезка времени посещения", alias="from"),
    to: int | None = Query(None, description="Конец отрезка времени посещения"),
) -> JSONResponse:
    """GET запрос на получение списка уникальных доменов."""
    visited_adapter = APP_CONTAINER.visited_urls_adapter()
    logger = APP_CONTAINER.logger()

    from_dttm = datetime.fromtimestamp(from_) if from_ else None
    to_dttm = datetime.fromtimestamp(to) if to else None

    logger.info(
        f"Trying to get visited domains with params from='{from_ or ''}' to='{to or ''}'..."
    )
    results = await visited_adapter.get_domains(from_dttm, to_dttm)

    return JSONResponse(
        content={"domains": list(results), "status": status.HTTP_200_OK},
        status_code=status.HTTP_200_OK,
    )
