FROM python:3.13-slim-bookworm

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"]