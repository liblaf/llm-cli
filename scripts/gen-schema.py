#!/usr/bin/env python
import json
from pathlib import Path

from llm_cli import llm


def main() -> None:
    Path("docs/schema/models.json").write_text(
        json.dumps(llm.Config.model_json_schema(), indent=2)
    )


if __name__ == "__main__":
    main()
