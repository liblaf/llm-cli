import functools

import llm_cli as lc


@functools.cache
def get_config() -> lc.config.Config:
    lc.config.init_litellm()
    return lc.config.Config()
