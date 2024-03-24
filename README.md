# Tracker of visited urls

Для работы сервиса необходимо:
* Версия Python 3.11 и выше
* Виртуальное окружение, для создания и установки зависимостей использовать команды:
    - python3 -m venv .venv
    - source .venv/bin/activate
    - poetry install
* Файл *env.json* с секретами:
    - SERVER_HOST (хост, на котором будет запущено приложение)
    - SERVER_PORT (порт, на котором будет запущено приложение)
    - DB_USER (имя пользователя БД)
    - DB_PASSWORD (пароль от учетной записи БД)
    - DB_APP_SCHEMA (схема БД)
    - DB_NAME (имя БД)
    - DB_HOST (хост БД)
    - DB_PORT (порт БД)
    - API_ENV (среда разработки)
    - API_TAG (тэг проекта)
* Запущенная БД Postgres с созданной схемой
* Актуальное состояние БД, обновление таблиц командой:
    - make migrations-up

---
Для запуска приложения возможно использование 2 вариаций:
* Запуск в контейнере [Makefile](Makefile): make docker-local-service
* Локальный запуск [Makefile](Makefile): make api

--- 
После обновления зависимостей poetry необходимо обновить *requirements.txt* командой:
* poetry export -o requirements.txt --without-hashes 

---
Команды запуска расположены в [Makefile](Makefile)

---
Ознакомиться со списком используемых библиотек можно в [pyproject.toml](pyproject.toml)