import openai
import openai.types.chat
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

from llm_cli import llm


async def output(cfg: llm.Config, prompt: str) -> str:
    client: openai.AsyncOpenAI = cfg.async_client
    resp: openai.AsyncStream[
        openai.types.chat.ChatCompletionChunk
    ] = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}], stream=True, model=cfg.model
    )
    completion: str = ""
    with Live() as live:
        async for chunk in resp:
            content: str | None = chunk.choices[0].delta.content
            if content is None:
                completion += "\n"
            else:
                completion += content
            live.update(Group(Panel(completion)))
    return completion
