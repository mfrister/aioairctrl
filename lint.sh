#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

black --check .
isort --check-only phipsair
mypy ./phipsair --show-error-codes
flake8 .
