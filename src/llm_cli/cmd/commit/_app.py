import asyncio

import typer

app = typer.Typer(name="commit")


@app.command()
def main() -> None:
    from ._main import main

    asyncio.run(main())
