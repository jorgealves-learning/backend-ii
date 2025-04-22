FROM python:3.12-slim

WORKDIR /workspace

RUN pip install poetry

COPY . .

COPY pyproject.toml poetry.lock /workspace/

RUN poetry install

RUN poetry run python manage.py collectstatic --noinput

CMD [ "poetry", "run","gunicorn","django_recap.wsgi:application","--bind","0.0.0.0:8000"]


