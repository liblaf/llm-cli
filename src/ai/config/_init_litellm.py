import dotenv

import ai.utils as aiu


def init_litellm() -> bool:
    return dotenv.load_dotenv(aiu.get_app_dir() / "litellm.env")
