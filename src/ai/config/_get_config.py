import functools

import ai.config as aic


@functools.cache
def get_config() -> aic.Config:
    return aic.Config()
