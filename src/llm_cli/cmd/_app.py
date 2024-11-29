import typer_di

import llm_cli.cmd as lcm
import llm_cli.utils as lcu

app = typer_di.TyperDI(name="llm-cli", no_args_is_help=True)
lcu.add_command(app, lcm.repo.app)
lcu.add_command(app, lcm.commit.app)
