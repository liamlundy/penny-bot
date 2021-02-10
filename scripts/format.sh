#!/usr/bin/env bash

set -e
set -x

black penny_bot tests
isort penny_bot tests
