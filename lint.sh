#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

black --check .
flake8 .
mypy ./phipsair
