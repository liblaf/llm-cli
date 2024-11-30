import ai
import ai.utils as aiu


async def main(*, long: bool = False) -> None:
    instruction: str = aiu.get_prompt("description-long" if long else "description")
    prompt: str = await aiu.repomix(instruction)
    await ai.output(prompt, prefix="<Answer>")
