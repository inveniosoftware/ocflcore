# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""Storage abstraction layer for the OCFL repository."""

from .base import Storage
from .filesystem import FileSystemStorage

__all__ = (
    "Storage",
    "FileSystemStorage",
)
