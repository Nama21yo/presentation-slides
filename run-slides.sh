#!/usr/bin/env zsh
set -euo pipefail

echo "run-slides.sh is deprecated. Use: just run" >&2
exec just run "$@"
