FROM python:3.11-slim AS base
WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
COPY src/ /app/src/
CMD ["python", "src/main.py"]

FROM base AS tests
COPY pyproject.toml /app/
COPY tests/ /app/tests/
RUN pip install --no-cache-dir ".[dev]"
CMD ["pytest", "-q"]

FROM base AS runtime
RUN useradd --create-home --uid 10001 app
USER 10001:10001
