#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

black --check .
flake8 .
isort --check-only phipsair
mypy ./phipsair
