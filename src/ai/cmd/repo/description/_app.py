import asyncio

import typer_di

import ai.utils as aiu

app = typer_di.TyperDI(name="description")


@app.command()
def main(_: None = typer_di.Depends(aiu.get_config)) -> None:
    from ._main import main

    asyncio.run(main())
