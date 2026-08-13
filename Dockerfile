FROM python:3.14-slim

RUN apt update && apt install -y \
    build-essential \
    libpq-dev

WORKDIR /app

COPY pyproject.toml .
RUN pip install .

COPY ./src .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
