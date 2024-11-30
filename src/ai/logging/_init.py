import functools

import ai


@functools.cache
def init() -> None:
    ai.logging.init_loguru()
