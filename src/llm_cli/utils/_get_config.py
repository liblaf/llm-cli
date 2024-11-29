from typing import Annotated

import typer

import llm_cli as lc
import llm_cli.config as lcc


def get_config(model: Annotated[str | None, typer.Option()] = None) -> None:
    lc.logging.init()
    cfg: lcc.Config = lcc.get_config()
    if model:
        cfg.completion.model = model
