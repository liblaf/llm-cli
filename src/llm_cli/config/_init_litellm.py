import dotenv

import llm_cli.utils as lu


def init_litellm() -> bool:
    return dotenv.load_dotenv(lu.get_app_dir() / "litellm.env")
