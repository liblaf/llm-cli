import asyncio

import typer_di

import llm_cli.utils as lcu

app = typer_di.TyperDI(name="description")


@app.command()
def main(_: None = typer_di.Depends(lcu.get_config)) -> None:
    from ._main import main

    asyncio.run(main())
