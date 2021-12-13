# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

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
