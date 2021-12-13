# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""OCFL storage hierarchies."""

from .base import StorageLayout
from .toplevel import TopLevelLayout

__all__ = (
    "StorageLayout",
    "TopLevelLayout",
)
