ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY tasks/implementations/python /app
RUN chmod +x /app/run.sh
