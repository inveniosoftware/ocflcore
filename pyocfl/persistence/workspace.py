# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Workspace for a transaction."""

from os.path import join


class Workspace:
    """Workspace for a transaction.

    Used to assemble an OCFL object or an OCFL version.
    """

    def __init__(self, storage, object_path):
        """Constructor for the workspace."""
        self.storage = storage
        self.object_path = object_path

    def write(self, content_path, stream):
        """Write a file in the workspace."""
        return self.storage.write(
            join(self.object_path, content_path),
            stream,
        )

    def setup(self):
        """Setup the workspace."""
        # TODO
        pass

    def teardown(self):
        """Teardown the workspace."""
        # TODO
        pass
