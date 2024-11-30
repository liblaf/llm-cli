import importlib.resources
from importlib.resources.abc import Traversable


def get_prompt(name: str) -> str:
    prompts_dir: Traversable = importlib.resources.files("ai.assets.prompts")
    fpath: Traversable = prompts_dir / f"{name}.md"
    return fpath.read_text()
