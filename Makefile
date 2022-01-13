.PHONY:run
run:
	docker-compose up
.PHONY:build
build:
	docker-compose build
.PHONY:start
start:
	docker-compose build && docker-compose up
#TODO smth wrong
#.PHONY:test
#test:
#	poetry install && poetry shell && poetry run pytest
