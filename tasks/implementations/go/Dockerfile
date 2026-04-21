ARG BUILD_IMAGE=golang:1.23-bookworm
ARG RUNTIME_IMAGE=debian:bookworm-slim
FROM ${BUILD_IMAGE} AS build
WORKDIR /app
COPY tasks/implementations/go /app
RUN cp tasks/*.go . && go build -o /bin/bench-go *.go
FROM ${RUNTIME_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
COPY --from=build /bin/bench-go /usr/local/bin/bench-go
COPY tasks/implementations/go/run.sh /app/run.sh
RUN chmod +x /app/run.sh
