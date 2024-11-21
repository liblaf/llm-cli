import typer

import llm_cli.cmd as lc
import llm_cli.utils as lu

app: typer.Typer = typer.Typer(name="llm-cli", no_args_is_help=True)
lu.add_command(app, lc.repo.app)
