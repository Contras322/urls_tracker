from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.models.base import BaseModel


class VisitedUrlsModel(BaseModel):
    """Модель истории посещения сайтов."""

    __tablename__ = "visited_urls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    link: Mapped[str] = mapped_column(String(512))
    domain: Mapped[str] = mapped_column(String(256))
    visit_dttm: Mapped[datetime] = mapped_column(DateTime)
