import json
import tempfile
from pathlib import Path

import llm_cli.utils as lcu


async def repomix(instruction: str | None = None) -> str:
    with tempfile.TemporaryDirectory() as tmpdir_:
        tmpdir = Path(tmpdir_)
        config_fpath: Path = tmpdir / "repomix.config.json"
        output_fpath: Path = tmpdir / "repomix-output.xml"
        config = {
            "output": {"filePath": str(output_fpath), "style": "xml"},
            "ignore": {
                "customPatterns": [
                    "**/.*",
                    "**/.*/**",
                    "**/*-lock.*",
                    "**/*.lock",
                    "**/CHANGELOG.md",
                    "**/pyrightconfig.json",
                ]
            },
        }
        if instruction:
            instruction_fpath: Path = tmpdir / "repomix-instruction.md"
            instruction_fpath.write_text(instruction)
            config["output"]["instructionFilePath"] = str(instruction_fpath)
        config_fpath.write_text(json.dumps(config))
        await lcu.run("repomix", "--config", config_fpath, check=True)
        return output_fpath.read_text()
