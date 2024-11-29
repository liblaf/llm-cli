import asyncio
import string

import git
import litellm
import typer

import llm_cli as lc
import llm_cli.utils as lu


async def main(path: list[str], *, verify: bool = True) -> None:
    await lu.run("git", "status")
    prompt_template = string.Template(lu.get_prompt("commit"))
    repo = git.Repo(search_parent_directories=True)
    diff: str = repo.git.diff("--cached", "--no-ext-diff", *path)
    files: str = repo.git.ls_files()
    prompt: str = prompt_template.substitute({"GIT_DIFF": diff, "GIT_FILES": files})
    resp: litellm.ModelResponse = await lc.output(prompt, prefix="<Answer>")
    choices: litellm.Choices = resp.choices[0]  # pyright: ignore [reportAssignmentType]
    message: str = lu.extract_between_tags(choices.message.content)
    proc: asyncio.subprocess.Process = await lu.run(
        "git",
        "commit",
        f"--message={message}",
        "--verify" if verify else "--no-verify",
        "--edit",
        check=False,
    )
    if proc.returncode:
        raise typer.Exit(proc.returncode)
