import json
import tempfile
from pathlib import Path

import ai.utils as aiu


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
        ignore_patterns: list[str] = aiu.get_ignore_patterns()
        config["ignore"]["customPatterns"] += ignore_patterns
        config_fpath.write_text(json.dumps(config))
        await aiu.run("repomix", "--config", config_fpath, check=True)
        return output_fpath.read_text()
