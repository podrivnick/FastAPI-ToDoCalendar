DC = docker-compose
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
EXEC = docker exec -it
DB_CONTAINER = postgres_calendar
LOGS = docker logs
ENV_FILE = --env-file .env
APP_CONTAINER = main-app
INTO_BASH_FOR_MIGRATE = /bin/bash -c
INTO_BASH = /bin/bash
CD_SRC = cd src &&
RUN_MIGRATION = poetry run alembic upgrade 8fc7334e3739

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV_FILE} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV_FILE} up -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH_FOR_MIGRATE} "${CD_SRC} ${RUN_MIGRATION}"

.PHONY: appbash
appbash:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH}