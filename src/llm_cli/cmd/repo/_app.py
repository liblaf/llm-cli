import asyncio
from typing import Annotated

import typer

app: typer.Typer = typer.Typer(name="repo", no_args_is_help=True)


@app.command()
def main(
    *,
    instruction: Annotated[
        str, typer.Option("-i", "--instruction", help="[description|topics]")
    ],
) -> None:
    from ._main import main

    asyncio.run(main(instruction=instruction))
