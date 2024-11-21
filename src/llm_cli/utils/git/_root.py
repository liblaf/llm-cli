from pathlib import Path

import git


def root() -> Path:
    repo: git.Repo = git.Repo(search_parent_directories=True)
    return Path(repo.working_tree_dir)  # pyright: ignore [reportArgumentType]
