import llm_cli as lc
import llm_cli.utils as lu


async def main() -> None:
    instruction: str = lu.get_prompt("topics")
    prompt: str = await lu.repomix(instruction)
    await lc.output(prompt, prefix="<Answer>")
