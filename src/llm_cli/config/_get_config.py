import functools

import llm_cli.config as lcc


@functools.cache
def get_config() -> lcc.Config:
    return lcc.Config()
