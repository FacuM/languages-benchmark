ARG BUILD_IMAGE=gcc:14-bookworm
ARG RUNTIME_IMAGE=gcc:14-bookworm
FROM ${BUILD_IMAGE} AS build
WORKDIR /app
COPY tasks/implementations/cpp /app
RUN g++ -O2 -std=c++20 dispatcher.cpp tasks/*.cpp -o /usr/local/bin/bench-cpp
FROM ${RUNTIME_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
COPY --from=build /usr/local/bin/bench-cpp /usr/local/bin/bench-cpp
COPY tasks/implementations/cpp/run.sh /app/run.sh
RUN chmod +x /app/run.sh
