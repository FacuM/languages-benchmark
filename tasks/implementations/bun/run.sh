#!/usr/bin/env bash
set -euo pipefail
exec bun run /app/dispatcher.js "$@"
