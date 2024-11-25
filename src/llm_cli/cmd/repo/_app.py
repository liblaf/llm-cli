import typer

import llm_cli.utils as lu
from llm_cli import cmd

app: typer.Typer = typer.Typer(name="repo", no_args_is_help=True)
lu.add_command(app, cmd.repo.description.app)
lu.add_command(app, cmd.repo.topics.app)
