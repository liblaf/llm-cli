#!/usr/bin/env python
import json
import subprocess
from pathlib import Path

import ai.config as aic


def main() -> None:
    output: Path = Path("docs/schema/config.json")
    output.write_text(json.dumps(aic.Config.model_json_schema()))
    subprocess.run(["prettier", "--write", output], check=True)


if __name__ == "__main__":
    main()
