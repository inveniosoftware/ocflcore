#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

black --check --diff ocflcore tests
python -m check_manifest --ignore ".*-requirements.txt"
python -m sphinx.cmd.build -qnN docs docs/_build/html
python -m pytest
