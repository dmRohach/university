APP_NAME=university

DATE := $(shell date)

.PHONY: migrate run stop
migrate:
	docker-compose up -d
	sleep 10
	docker exec uvicorn alembic revision --autogenerate -m "$(DATE)"
	docker exec uvicorn alembic upgrade head
	docker-compose stop

run:
	docker-compose up

stop:
	docker-compose stop

build-service:
	docker-compose build

build: | build-service migrate

tests:
	docker-compose up -d
	docker exec uvicorn pytest
	docker-compose stop


