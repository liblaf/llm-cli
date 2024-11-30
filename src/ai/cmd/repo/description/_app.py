import asyncio
from typing import Annotated

import typer
import typer_di

import ai.utils as aiu

app = typer_di.TyperDI(name="description")


@app.command()
def main(
    *,
    long: Annotated[bool, typer.Option()] = False,
    _: None = typer_di.Depends(aiu.get_config),
) -> None:
    from ._main import main

    asyncio.run(main(long=long))
