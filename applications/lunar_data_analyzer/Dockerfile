FROM python:3.13-slim-bookworm

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "python", "./app/main.py"]