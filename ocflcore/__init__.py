# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""Pythonic API for interacting with an OCFL storage root."""

from .domain.layouts import StorageLayout, TopLevelLayout
from .domain.ocflobj import OCFLObject, OCFLVersion
from .domain.root import StorageRoot
from .persistence.repository import OCFLRepository
from .persistence.storage import FileSystemStorage
from .stream import StreamDigest
from .version import __version__

__all__ = (
    "__version__",
    "FileSystemStorage",
    "OCFLObject",
    "OCFLRepository",
    "OCFLVersion",
    "StorageLayout",
    "StorageRoot",
    "StreamDigest",
    "TopLevelLayout",
)
