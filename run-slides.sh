#!/usr/bin/env zsh
set -euo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
MANIM_SLIDES_BIN="$PROJECT_DIR/.venv/bin/manim-slides"

if [[ ! -x "$MANIM_SLIDES_BIN" ]]; then
  echo "Error: '$MANIM_SLIDES_BIN' was not found or is not executable." >&2
  echo "Make sure your virtual environment is created and dependencies are installed." >&2
  exit 1
fi

# Force software decode to avoid Qt FFmpeg CUDA hwaccel probe warnings on unsupported GPUs.
export QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none

exec "$MANIM_SLIDES_BIN" "$@"
