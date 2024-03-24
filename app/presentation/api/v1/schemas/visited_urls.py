from pydantic import BaseModel


class VisitedUrlsSchema(BaseModel):
    """Список ресурсов, посещенных сотрудником."""

    links: list[str]
