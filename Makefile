.PHONY:run
run:
	docker-compose up
.PHONY:build
build:
	docker-compose build
.PHONY:start
start:
	docker-compose build && docker-compose up
.PHONY:test
test:
	poetry run pytest
