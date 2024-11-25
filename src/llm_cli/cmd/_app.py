import typer

import llm_cli.utils as lu
from llm_cli import cmd

app: typer.Typer = typer.Typer(name="llm-cli", no_args_is_help=True)
lu.add_command(app, cmd.repo.app)
lu.add_command(app, cmd.commit.app)
