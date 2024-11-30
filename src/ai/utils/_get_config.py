from typing import Annotated

import typer

import ai
import ai.config as aic


def get_config(model: Annotated[str | None, typer.Option()] = None) -> None:
    ai.logging.init()
    cfg: aic.Config = aic.get_config()
    if model:
        cfg.completion.model = model
