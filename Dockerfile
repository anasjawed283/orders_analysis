# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system --deploy

COPY . /app

CMD ["python", "orders_analysis.py"]
