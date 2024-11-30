import functools
from pathlib import Path

import typer


@functools.cache
def get_app_dir() -> Path:
    return Path(typer.get_app_dir("ai-cli"))
