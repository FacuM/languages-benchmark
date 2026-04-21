ARG BASE_IMAGE=php:8.4-cli
FROM ${BASE_IMAGE}
RUN set -eux; \
    legacy_apt=''; \
    if [ -f /etc/apt/sources.list ]; then \
      if grep -Eq 'buster|stretch|jessie' /etc/apt/sources.list; then \
        sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list; \
        sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list; \
        sed -i '/buster-updates/d;/stretch-updates/d;/jessie-updates/d' /etc/apt/sources.list; \
        printf 'Acquire::Check-Valid-Until \"false\";\n' > /etc/apt/apt.conf.d/99no-check-valid; \
        legacy_apt='-o Acquire::AllowInsecureRepositories=true -o Acquire::AllowDowngradeToInsecureRepositories=true'; \
      fi; \
    fi; \
    sh -lc "apt-get $legacy_apt update"; \
    sh -lc "apt-get $legacy_apt install -y --allow-unauthenticated --no-install-recommends time sqlite3"; \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY tasks/implementations/php /app
RUN chmod +x /app/run.sh
