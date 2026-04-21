#!/usr/bin/env bash
set -euo pipefail
exec java --add-modules jdk.httpserver -cp /app/classes Dispatcher "$@"
