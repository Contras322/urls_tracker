from pydantic import BaseModel, Field


class VersionSchema(BaseModel):
    """Схема с версией приложения."""

    version: str = Field(examples=["0.1.2"])
