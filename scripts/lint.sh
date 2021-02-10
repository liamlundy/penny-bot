#!/usr/bin/env bash

set -e
set -x

mypy penny_bot
flake8 penny_bot tests
black penny_bot tests --check
isort penny_bot tests --check-only
