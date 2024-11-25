import asyncio

import typer

app: typer.Typer = typer.Typer(name="description", no_args_is_help=True)


@app.command()
def main() -> None:
    from ._main import main

    asyncio.run(main())
