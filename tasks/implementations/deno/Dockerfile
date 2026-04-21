ARG BASE_IMAGE=denoland/deno:2.7.6
FROM ${BASE_IMAGE}
USER root
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY tasks/implementations/node /app
COPY tasks/implementations/deno/run.sh /app/run.sh
RUN chmod +x /app/run.sh
