import llm_cli as lc
import llm_cli.utils as lcu


async def main() -> None:
    instruction: str = lcu.get_prompt("topics")
    prompt: str = await lcu.repomix(instruction)
    await lc.output(prompt, prefix="<Answer>")
