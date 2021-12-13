#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

black --check --diff ocflcore tests
python -m check_manifest --ignore ".*-requirements.txt"
python -m sphinx.cmd.build -qnN docs docs/_build/html
python -m pytest
