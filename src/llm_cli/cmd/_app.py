from typing import Annotated

import typer

import llm_cli as lc
import llm_cli.cmd as lcm
import llm_cli.config as lcc
import llm_cli.utils as lcu

app: typer.Typer = typer.Typer(name="llm-cli", no_args_is_help=True)
lcu.add_command(app, lcm.repo.app)
lcu.add_command(app, lcm.commit.app)


@app.callback()
def init(model: Annotated[str | None, typer.Option()] = None) -> None:
    lc.logging.init()
    cfg: lcc.Config = lcc.get_config()
    if model:
        cfg.completion.model = model
