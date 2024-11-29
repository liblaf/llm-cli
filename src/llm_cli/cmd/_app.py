import typer

import llm_cli.utils as lcu
from llm_cli import cmd as lcc

app: typer.Typer = typer.Typer(name="llm-cli", no_args_is_help=True)
lcu.add_command(app, lcc.repo.app)
lcu.add_command(app, lcc.commit.app)
