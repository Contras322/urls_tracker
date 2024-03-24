import click

from cli.migrations import migrations
from cli.start import start
from utils.settings import dev


@click.group()
def main() -> None:
    """Команда управления приложением."""

    # Установка переменных окружения из env.json для удобства разработки.
    dev.set_env()


main.add_command(start)
main.add_command(migrations)

main()
