import ai
import ai.utils as aiu


async def main() -> None:
    instruction: str = aiu.get_prompt("description")
    prompt: str = await aiu.repomix(instruction)
    await ai.output(prompt, prefix="<Answer>")
