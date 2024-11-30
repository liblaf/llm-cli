import asyncio
import string

import git
import litellm
import typer

import ai
import ai.utils as aiu


async def main(path: list[str], *, verify: bool = True) -> None:
    await aiu.run("git", "status", *path)
    prompt_template = string.Template(aiu.get_prompt("commit"))
    repo = git.Repo(search_parent_directories=True)
    diff: str = repo.git.diff("--cached", "--no-ext-diff", *path)
    files: str = repo.git.ls_files()
    prompt: str = prompt_template.substitute({"GIT_DIFF": diff, "GIT_FILES": files})
    resp: litellm.ModelResponse = await ai.output(prompt, prefix="<Answer>")
    content: str = litellm.get_content_from_model_response(resp)
    message: str = aiu.extract_between_tags(content)
    proc: asyncio.subprocess.Process = await aiu.run(
        "git",
        "commit",
        f"--message={message}",
        "--verify" if verify else "--no-verify",
        "--edit",
        check=False,
    )
    if proc.returncode:
        raise typer.Exit(proc.returncode)
