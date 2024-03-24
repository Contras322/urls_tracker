import json
import os

from utils.base_dir import BASE_DIR

_JSON_FILE = BASE_DIR / "env.json"
_ENV_FILE_ENCODING = "utf-8"


def set_env():
    """Задать переменные окружения из файла env.json."""

    if not os.path.isfile(_JSON_FILE):
        return

    with open(_JSON_FILE, encoding=_ENV_FILE_ENCODING) as env_json:
        data = env_json.read()
        try:
            env_vars = json.loads(data)
        except json.decoder.JSONDecodeError as ex:
            raise json.decoder.JSONDecodeError(
                f"User application config decoding error: {_JSON_FILE}", doc=data, pos=ex.pos
            ) from ex

        for key, value in env_vars.items():
            os.environ[key] = value

        print(f"Set vars from user application config: {_JSON_FILE}.")
