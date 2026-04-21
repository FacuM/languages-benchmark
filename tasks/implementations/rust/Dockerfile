ARG BUILD_IMAGE=rust:1.82-slim-bookworm
ARG RUNTIME_IMAGE=debian:bookworm-slim
FROM ${BUILD_IMAGE} AS build
WORKDIR /app
COPY tasks/implementations/rust /app
RUN cargo build --release
FROM ${RUNTIME_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
COPY --from=build /app/target/release/bench-rust /usr/local/bin/bench-rust
COPY tasks/implementations/rust/run.sh /app/run.sh
RUN chmod +x /app/run.sh
