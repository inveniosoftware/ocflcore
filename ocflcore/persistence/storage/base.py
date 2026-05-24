# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

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
