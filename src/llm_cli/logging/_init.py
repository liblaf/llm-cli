import functools

import llm_cli as lc


@functools.cache
def init() -> None:
    lc.logging.init_loguru()
