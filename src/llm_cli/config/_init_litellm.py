import dotenv

import llm_cli.utils as lcu


def init_litellm() -> bool:
    return dotenv.load_dotenv(lcu.get_app_dir() / "litellm.env")
