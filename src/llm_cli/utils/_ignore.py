import itertools
from collections.abc import Iterable
from os import PathLike
from pathlib import Path

import llm_cli.utils as lcu


def get_ignore_patterns(
    root: str | PathLike[str] | None = None,
    ignore_filename: str | Iterable[str] = ".aiignore",
) -> list[str]:
    root: Path = lcu.working_dir(root)
    ignore_filename: list[str] = lcu.as_list(ignore_filename)
    patterns: list[str] = []
    for file in itertools.chain(*map(root.rglob, ignore_filename)):
        for line in file.read_text().splitlines():
            stripped: str = line.strip()
            if stripped and not stripped.startswith("#"):
                patterns.append(stripped)
    return patterns
