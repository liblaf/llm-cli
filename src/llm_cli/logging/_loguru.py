import functools
import inspect
import logging
import sys
import types

from loguru import logger

import llm_cli as lc


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame: types.FrameType | None
        depth: int
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


@functools.cache
def init_loguru() -> None:
    lc.logging.fix_litellm()
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": "INFO",
                "filter": {"httpx": "WARNING", "litellm": "WARNING"},
            }
        ]
    )
