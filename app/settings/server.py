from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    """Настройки uvicorn сервера."""

    # Путь до ASGI в формате "<module>:<attribute>"
    app: str = "app.presentation.api.__main__:create_app"
    # Флаг запуска сервера в режиме разработки
    debug: bool = Field(default=False, serialization_alias="reload")
    # Уровень логирования
    log_level: str = "info"
    # Хост приложения
    host: str
    # Порт приложения
    port: int

    model_config = SettingsConfigDict(env_prefix="server_")
