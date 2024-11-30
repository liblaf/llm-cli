import importlib.resources
import json
import tempfile
from pathlib import Path

import ai
import ai.utils as aiu


async def main(instruction: str) -> None:
    with tempfile.TemporaryDirectory() as tmpdir_:
        tmpdir: Path = Path(tmpdir_)
        config_fpath: Path = tmpdir / "repomix.config.json"
        output_file_path: Path = tmpdir / "repomix-output.xml"
        instruction_fpath: Path = tmpdir / "repomix-instruction.md"
        instruction_fpath.write_text(_get_instruction(instruction))
        config_fpath.write_text(_get_config(tmpdir, instruction_fpath))
        await aiu.run("repomix", "--config", config_fpath)
        prompt: str = output_file_path.read_text()
    await ai.output(prompt, prefix="<answer>", stop="</answer>")


def _get_config(tmpdir: Path, instruction_fpath: Path) -> str:
    return json.dumps(
        {
            "output": {
                "filePath": str(tmpdir / "repomix-output.xml"),
                "style": "xml",
                "instructionFilePath": str(instruction_fpath),
            },
            "ignore": {
                "customPatterns": [
                    "**/.*",
                    "**/.*/**",
                    "**/*-lock.*",
                    "**/*.lock",
                    "**/pyrightconfig.json",
                ]
            },
        }
    )


def _get_instruction(instruction: str) -> str:
    instruction_fpath: Path = Path(instruction)
    if instruction_fpath.is_file():
        return Path(instruction).read_text()
    return importlib.resources.read_text(
        "ai_cli.assets.instructions", f"{instruction}.md"
    )
