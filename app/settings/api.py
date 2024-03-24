from typing import TYPE_CHECKING

from pydantic_settings import BaseSettings, SettingsConfigDict

if TYPE_CHECKING:
    from utils.pyproject import PyProjectData


class ApiEnvSettings(BaseSettings):
    """Настройки API из переменных окружения."""

    # Имя среды.
    tag: str | None = None
    # Тег среды.
    env: str
    # Версия приложения.
    version: str | None = None
    # Пути игнорируемые при access логах и метриках.
    ignored_paths: set[str] = {"/system/liveness", "/system/readiness", "/metrics"}

    model_config = SettingsConfigDict(env_prefix="api_")


class ApiSettings:
    """Настройки API."""

    def __init__(self, api_settings: "ApiEnvSettings", py_project_data: "PyProjectData"):
        self.tag = api_settings.tag or py_project_data.get_app_name()
        self.env = api_settings.env
        self.version = api_settings.version or py_project_data.get_app_version()
        self.title = f"{self.tag}_{self.env}".replace("-", "_")
        self.ignored_paths = api_settings.ignored_paths
