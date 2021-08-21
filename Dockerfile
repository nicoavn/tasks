# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY pyproject.toml /code

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

