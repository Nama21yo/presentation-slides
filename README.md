# Presentation Slides (Manim + manim-slides)

This repository contains a slide deck built with **Manim** and presented with **manim-slides**.
It is designed to grow over time as new slides are added.

## Project layout

- `slides/` — Python scene files (`slide1_*.py`, `slide2_*.py`, ...)
- `media/` — generated render assets (videos, images, cache)
- `justfile` — primary command entrypoint for presenting the full deck
- `requirements.txt` / `pyproject.toml` — Python dependencies

## Requirements

- Python 3.14+ (project currently uses `.venv`)
- FFmpeg installed and available on PATH
- Dependencies installed in virtual environment

## Setup

Create/activate your virtual environment and install dependencies (using `uv`):

```zsh
uv pip install --python .venv/bin/python -r requirements.txt
```

## Render a single slide scene

Example:

```zsh
.venv/bin/manim -ql slides/slide1_title.py TitleSlide
```

Use `-qh`/`-qm` for higher quality when needed.

## Present the full deck

The recommended way is the `justfile` recipe:

```zsh
just run
```

This recipe sets:

- `QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none`

to avoid noisy CUDA hardware-decoding warnings on unsupported systems.

## Adding new slides (future-proof workflow)

1. Add a new scene file in `slides/`, following naming convention:
   - `slide12_topic.py`, `slide13_topic.py`, etc.
2. Define a class that extends `Slide`, e.g. `class NewTopicSlide(Slide): ...`
3. Render once with Manim to generate/update slide config JSON.
4. Append the new scene class name to the `justfile` `run` recipe in presentation order.
5. Commit both source files and generated slide config files.

## Notes

- Keep scene names descriptive and stable; `manim-slides` references class names.
- If playback logs show CUDA decode warnings, keep using `just run` (already configured to suppress them).
- `media/` is generated output and is ignored in git.
