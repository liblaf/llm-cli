#!/usr/bin/env python
import json
import subprocess
from pathlib import Path

import llm_cli.config as lcc


def main() -> None:
    output: Path = Path("docs/schema/config.json")
    output.write_text(json.dumps(lcc.Config.model_json_schema()))
    subprocess.run(["prettier", "--write", output], check=True)


if __name__ == "__main__":
    main()
