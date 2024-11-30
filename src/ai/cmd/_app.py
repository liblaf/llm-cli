import typer_di

import ai.cmd as aim
import ai.utils as aiu

app = typer_di.TyperDI(name="ai", no_args_is_help=True)
aiu.add_command(app, aim.repo.app)
aiu.add_command(app, aim.commit.app)
