activate:
	source run.sh; activate

install:
	source run.sh; install

run:
	source run.sh; run $(port)

run-docker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0
else
	flask run -p $(port) -h 0.0.0.0
endif

docker-dev-up:
	docker compose -f docker-compose.dev.yml up --build -d

docker-dev-down:
	docker compose -f docker-compose.dev.yml down

docker-up:
	docker compose up --build

docker-down:
	docker compose down

docker-build:
	docker build -t python-calculator-api:v0.0.1 .

docker-run:
	docker run -d -p 4000:4000 python-calculator-api:v0.0.1

docker-stop:
	docker stop python-calculator-api