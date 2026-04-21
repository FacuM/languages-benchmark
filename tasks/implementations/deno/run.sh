#!/usr/bin/env bash
set -euo pipefail
exec deno run -A /app/dispatcher.js "$@"
