import asyncio
from typing import Annotated

import typer

app = typer.Typer(name="commit")


@app.command()
def main(
    path: Annotated[list[str] | None, typer.Argument()] = None,
    *,
    default_exclude: Annotated[bool, typer.Option()] = True,
    verify: Annotated[bool, typer.Option()] = True,
) -> None:
    from ._main import main

    path: list[str] = path or []
    if default_exclude:
        path += [":!*-lock.*", ":!*.lock*", ":!*.cspell.*"]
    asyncio.run(main(path, verify=verify))
