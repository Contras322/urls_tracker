import alembic.config
import click

from utils.base_dir import BASE_DIR

ALEMBIC_CONFIG_FILE = BASE_DIR / "migrations" / "alembic.ini"


@click.group()
def migrations() -> None:
    """Миграции базы данных."""


@migrations.command()
@click.option("--revision", default="head", type=str)
def up(revision: str) -> None:  # pylint: disable=invalid-name
    """Мигрировать до заданной миграции в сторону обновления."""
    alembic_args = ["-c", str(ALEMBIC_CONFIG_FILE), "upgrade", revision.strip()]
    alembic.config.main(argv=alembic_args)


@migrations.command()
@click.option("--revision", default="-1")
def down(revision: str) -> None:
    """Откатиться до заданной миграции."""
    alembic_args = ["-c", str(ALEMBIC_CONFIG_FILE), "downgrade", revision.strip()]
    alembic.config.main(argv=alembic_args)


@migrations.command()
@click.argument("name", type=str)
def make(name: str) -> None:
    """Создать миграцию с заданным именем."""
    alembic_args = ["-c", str(ALEMBIC_CONFIG_FILE), "revision", "--autogenerate", "--message", name]
    alembic.config.main(argv=alembic_args)
