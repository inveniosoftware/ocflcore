# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Storage abstraction layer for the OCFL repository."""

from .base import Storage
from .filesystem import FileSystemStorage

__all__ = (
    "Storage",
    "FileSystemStorage",
)