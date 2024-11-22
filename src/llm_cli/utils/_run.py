import asyncio.subprocess as asp
import subprocess
from os import PathLike

type _StrOrBytesPath = str | bytes | PathLike[str] | PathLike[bytes]


async def run(
    program: _StrOrBytesPath, *args: _StrOrBytesPath, check: bool = True
) -> None:
    proc: asp.Process = await asp.create_subprocess_exec(program, *args)
    returncode: int = await proc.wait()
    if check and returncode != 0:
        raise subprocess.CalledProcessError(returncode, [program, *args])
