import importlib.resources


def get_prompt(name: str) -> str:
    prompts_dir = importlib.resources.files("llm_cli.assets.prompts")
    fpath = prompts_dir / f"{name}.md"
    return fpath.read_text()
