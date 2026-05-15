#!/bin/bash

set -exo pipefail

export RAWPY_USE_SYSTEM_LIBRAW=1

python -m pip install . -vv --no-deps --no-build-isolation
