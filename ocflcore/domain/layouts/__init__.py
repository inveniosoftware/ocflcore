# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""OCFL storage hierarchies."""

from .base import StorageLayout
from .toplevel import TopLevelLayout

__all__ = (
    "StorageLayout",
    "TopLevelLayout",
)
