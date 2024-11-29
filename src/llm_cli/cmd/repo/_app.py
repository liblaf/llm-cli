import typer_di

import llm_cli.utils as lcu
from llm_cli import cmd as lcm

app = typer_di.TyperDI(name="repo", no_args_is_help=True)
lcu.add_command(app, lcm.repo.description.app)
lcu.add_command(app, lcm.repo.topics.app)
