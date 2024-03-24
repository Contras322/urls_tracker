import click
import uvicorn

from app.container import APP_CONTAINER


@click.group()
def start() -> None:
    """Запустить один из выбранных сервисов."""


@start.command()
def api() -> None:
    """API-сервис."""
    uvicorn.run(**APP_CONTAINER.server_settings().model_dump(by_alias=True))
