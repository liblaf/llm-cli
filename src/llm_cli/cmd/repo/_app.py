import typer

import llm_cli.utils as lcu
from llm_cli import cmd as lcm

app: typer.Typer = typer.Typer(name="repo", no_args_is_help=True)
lcu.add_command(app, lcm.repo.description.app)
lcu.add_command(app, lcm.repo.topics.app)
