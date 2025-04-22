startproject:
	poetry run django-admin startapp $(APP) .
startapp:
	docker compose run --rm web poetry run python manage.py startapp $(APP)
build:
	docker compose build
down:
	docker compose down
clean:
	docker compose down --volumes
run: build
	docker compose up --force-recreate
migrate:
	docker compose run --rm web poetry run python manage.py migrate
makemigrations:
	docker compose run --rm web poetry run python manage.py makemigrations
