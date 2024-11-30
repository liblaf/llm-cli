import importlib
import logging


def fix_litellm() -> None:
    importlib.import_module("litellm._logging")
    for name in ["LiteLLM Proxy", "LiteLLM Router", "LiteLLM"]:
        logging.getLogger(name).handlers.clear()
