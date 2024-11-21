import importlib.resources
import json
import subprocess
import tempfile
from pathlib import Path

from llm_cli import llm


async def main(instruction: str) -> None:
    with tempfile.TemporaryDirectory() as tmpdir_:
        tmpdir: Path = Path(tmpdir_)
        config_fpath: Path = tmpdir / "repomix.config.json"
        output_file_path: Path = tmpdir / "repomix-output.xml"
        instruction_fpath: Path = tmpdir / "repomix-instruction.md"
        instruction_fpath.write_text(_get_instruction(instruction))
        config_fpath.write_text(_get_config(tmpdir, instruction_fpath))
        subprocess.run(["repomix", "--config", config_fpath], check=True, text=True)
        prompt: str = output_file_path.read_text()
    cfg: llm.Config = llm.Config()
    result: str = await llm.output(cfg, prompt)
    # TODO


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
        "llm_cli.assets.instructions", f"{instruction}.md"
    )
