# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""Storage layout with object in the storage root."""

from .base import StorageLayout


class TopLevelLayout(StorageLayout):
    """Simple top-level layout class."""

    description = "Top-level hierarchy"
    extension = None

    def path_for(self, obj):
        """Top-level just uses the object ID."""
        return obj.id
