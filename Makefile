.DEFAULT_GOAL = api

CURRENT_DIRECTORY = $(shell pwd)
LOCAL_IMAGE = "tracker:1"

# Компоненты
api:
	python -m cli start api


# Миграции
migrations-make:
	python -m cli migrations make $(NAME)

migrations-up:
	python -m cli migrations up

migrations-down:
	python -m cli migrations down

# Тесты, линтеры, форматеры
tests-linters:
	linters/run_tests_linters.sh

unit-tests:
	pytest ./tests

formatters: black isort

black:
	black ./

isort:
	isort ./


docker-local-service:
	export IMAGE=$(LOCAL_IMAGE) \
	&& docker build --target app -t $(LOCAL_IMAGE) . \
	&& docker-compose -f ./run/docker-compose.yml up app
