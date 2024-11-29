import logging

import litellm  # noqa: F401


def fix_litellm() -> None:
    for name in ["LiteLLM Proxy", "LiteLLM Router", "LiteLLM"]:
        logging.getLogger(name).handlers.clear()
