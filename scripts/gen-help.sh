#!/bin/bash
set -o errexit -o nounset -o pipefail

typer ai utils docs --output docs/help.md
prettier --write docs/help.md
markdownlint --fix docs/help.md
