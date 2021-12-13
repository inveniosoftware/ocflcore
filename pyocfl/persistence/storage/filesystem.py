# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""File system storage implementations for OCFL."""

import shutil
from os import makedirs
from os.path import dirname, join

from .base import Storage


class FileSystemStorage(Storage):
    """File system storage."""

    def __init__(self, root_path):
        """Construct the file system.

        :param root_path: Path to the storage root.
        """
        self._root = root_path

    def _p(self, path):
        """Absolute path."""
        return join(self._root, path)

    def write(self, file_path, stream):
        """Write stream to the given file path in the storage root.

        Automatically creates missing directories, and uses a 1MB chunk size.
        """
        file_path = self._p(file_path)
        dir_path = dirname(file_path)
        if dir_path:
            makedirs(dir_path, exist_ok=True)

        chunk_size = 10 * 1024 * 1024  # 10mb

        with open(file_path, "wb") as fp:
            # Write in chunks
            while 1:
                chunk = stream.read(chunk_size)
                if not chunk:
                    break
                fp.write(chunk)

    def move(self, other_storage, path):
        """Move between storage systems."""
        other_path = join(other_storage._root, path)
        our_path = self._p(path)
        shutil.move(other_path, our_path)
        # TODO: support other storage types
