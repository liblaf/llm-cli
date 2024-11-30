from os import PathLike
from pathlib import Path

import git


def working_dir(working_dir: str | PathLike[str] | None = None) -> Path:
    if working_dir is not None:
        return Path(working_dir)
    try:
        repo = git.Repo(search_parent_directories=True)
        return Path(repo.working_dir)
    except git.InvalidGitRepositoryError:
        return Path.cwd()
