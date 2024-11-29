from collections.abc import Callable, Sequence
from typing import Any

import litellm
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

import llm_cli as lc
import llm_cli.utils as lu


async def output(
    prompt: str,
    *,
    prefix: str | None = None,
    sanitize: Callable[[str], str] | None = lu.extract_between_tags,
    stop: str | Sequence[str] | None = None,
    title: str | None = None,
) -> litellm.ModelResponse:
    cfg: lc.Config = lc.get_config()
    messages: list[dict[str, Any]] = [{"role": "user", "content": prompt}]
    if prefix:
        messages.append({"role": "assistant", "content": prefix, "prefix": True})
    stream: litellm.CustomStreamWrapper = await litellm.acompletion(
        model=cfg.model,
        messages=messages,
        stream=True,
        stream_options={"include_usage": True},
        stop=stop,
    )  # pyright: ignore [reportAssignmentType]
    chunks: list[litellm.ModelResponse] = []
    response: litellm.ModelResponse = litellm.ModelResponse()
    with Live() as live:
        async for chunk in stream:
            chunk: litellm.ModelResponse
            chunks.append(chunk)
            response = litellm.stream_chunk_builder(chunks)  # pyright: ignore [reportAssignmentType]
            choices: litellm.Choices = response.choices[0]  # pyright: ignore [reportAssignmentType]
            content: str = choices.message.content or ""
            if prefix and not content.startswith(prefix):
                content = prefix + content
            if sanitize:
                content = sanitize(content)
            live.update(
                Group(
                    Panel(content, title=title, title_align="left"),
                    Panel(lc.pretty_usage(response)),
                )
            )
    return response
