FROM python:3.13-slim

WORKDIR /workspace

COPY pyproject.toml poetry.lock /workspace/

RUN pip install --upgrade pip && pip install poetry

COPY . .

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "django_graphql.main:app"]