import typer_di

import ai.utils as aiu
from ai import cmd as aim

app = typer_di.TyperDI(name="repo", no_args_is_help=True)
aiu.add_command(app, aim.repo.description.app)
aiu.add_command(app, aim.repo.topics.app)
