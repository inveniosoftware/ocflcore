# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Storage layout with object in the storage root."""

from .base import StorageLayout


class TopLevelLayout(StorageLayout):
    """Simple top-level layout class."""

    description = "Top-level hierarchy"
    extension = None

    def path_for(self, obj):
        """Top-level just uses the object ID."""
        return obj.id
