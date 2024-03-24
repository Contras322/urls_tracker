from datetime import datetime
from urllib.parse import urlparse

from pydantic import BaseModel, ConfigDict


class VisitedUrl(BaseModel):
    """Сущность записи о посещении ресурса."""

    link: str
    visit_dttm: datetime

    model_config = ConfigDict(from_attributes=True, validate_default=True, validate_assignment=True)

    @property
    def domain(self) -> str:
        """Домен посещенного ресурса."""
        return urlparse(self.link).netloc
