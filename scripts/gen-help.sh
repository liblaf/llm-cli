#!/bin/bash
set -o errexit -o nounset -o pipefail

typer llm_cli utils docs --output docs/help.md
prettier --write docs/help.md
