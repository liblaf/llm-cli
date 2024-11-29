import typer

import llm_cli.utils as lcu
from llm_cli import cmd as lcc

app: typer.Typer = typer.Typer(name="repo", no_args_is_help=True)
lcu.add_command(app, lcc.repo.description.app)
lcu.add_command(app, lcc.repo.topics.app)
