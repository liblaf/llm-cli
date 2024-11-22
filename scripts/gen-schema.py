#!/usr/bin/env python
import json
import subprocess
from pathlib import Path

import llm_cli as lc


def main() -> None:
    output: Path = Path("docs/schema/config.json")
    output.write_text(json.dumps(lc.Config.model_json_schema()))
    subprocess.run(["prettier", "--write", output], check=True)


if __name__ == "__main__":
    main()
