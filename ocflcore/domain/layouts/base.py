# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Logical representation of an OCFL storage root."""

import json


class StorageLayout:
    """Base class for storage root hierarchies layouts."""

    description = None
    extension = None

    @property
    def data(self):
        """Get a dictionary for the ocfl_layout.json file."""
        result = {}
        if self.description is not None:
            result["description"] = self.description
        if self.extension is not None:
            result["extension"] = self.extension
        return result or None

    @property
    def json_bytes(self):
        """Get the JSON serialization of this storage root."""
        data = self.data
        return json.dumps(data).encode("utf-8") if data is not None else None

    def path_for(self, obj):
        """Compute path for a given object."""
        raise NotImplementedError()
