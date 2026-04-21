ARG BUILD_IMAGE=eclipse-temurin:21-jdk-jammy
ARG RUNTIME_IMAGE=eclipse-temurin:21-jdk-jammy
FROM ${BUILD_IMAGE} AS build
WORKDIR /app
COPY tasks/implementations/java /app
RUN mkdir -p /app/classes && javac --add-modules jdk.httpserver -d /app/classes Dispatcher.java tasks/*.java
FROM ${RUNTIME_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends time sqlite3 && rm -rf /var/lib/apt/lists/*
COPY --from=build /app/classes /app/classes
COPY tasks/implementations/java/run.sh /app/run.sh
RUN chmod +x /app/run.sh
