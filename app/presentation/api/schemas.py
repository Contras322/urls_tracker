from pydantic import BaseModel


class ResponseErrorSchema(BaseModel):
    """Схема ответа с ошибкой."""

    message: str
