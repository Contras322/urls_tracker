from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    """Класс настройки подключения к базе данных."""

    # Схема в url в БД.
    url_schema: str = "postgresql"
    # Драйвер подключения к БД.
    async_driver: str = "asyncpg"
    # Пользователь БД.
    user: str
    # Пароль БД.
    password: str
    # Хост БД.
    host: str
    # Порт БД.
    port: str
    # Имя БД.
    name: str

    # Схема приложения в БД.
    app_schema: str

    @property
    def url(self) -> str:
        """Ссылка для подключения к БД с использованием асинхронного драйвера."""
        schema = f"{self.url_schema}+{self.async_driver}"
        return f"{schema}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    model_config = SettingsConfigDict(env_prefix="db_")
