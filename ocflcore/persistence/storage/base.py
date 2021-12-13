# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Storage implementations for OCFL."""


class Storage:
    """Base class for the storage APIs."""

    def write(self, file_path, stream):
        """Write stream to the given file path.

        File path is relative to the OCFL storage root.
        """
        raise NotImplementedError

    def move(self, other_storage, path):
        """Move an director from one storage to another."""
        raise NotImplementedError
