# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Transaction used for as close as possible for atomic operations.

Transactions works by assembling the OCFL object or OCFL version in a separate
workspace and then transfer it into the OCFL stroage root in as safe manner as
possible. It also keeps a transaction log of commands executed (e.g. writing),
so that in case a commands fails, we can undo executed commands.

The goal of the transaction is to have as close to atomic operations as
possible, but since we're dealing with file systems, we're not gonna have
ACID properties like in a database.

See https://ocfl.io/1.0/implementation-notes/#segregating-objects-in-flight
"""

from .commands import WriteCommand
from .workspace import Workspace


class Transaction:
    """A transaction on the OCFL storage root.

    A transaction is a context mananger.
    """

    def __init__(self, repository, obj):
        """Initialize the transaction."""
        self._log = []
        self.repository = repository
        self.obj = obj
        self.object_path = self.repository.root.layout.path_for(self.obj)
        self.workspace = None

    #
    # Content manager
    #
    def __enter__(self):
        """Enter the transaction."""
        self.workspace = self.create_workspace()
        self.workspace.setup()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit the transaction and rollback on exceptions."""
        if exc_type is not None:
            self.rollback()
        self.workspace.teardown()
        self.workspace = None

    #
    # Transaction log
    #
    def _register(self, cmd):
        """Register a command on the transaction log."""
        self._log.append(cmd)

    #
    # Transaction API
    #
    def create_workspace(self):
        """Create a workspace for the transaction."""
        workspace = Workspace(
            self.repository.workspace_storage,
            self.object_path,
        )
        workspace.setup()
        return workspace

    def write(self, content_path, stream):
        """Write a content path in the workspace."""
        self._register(WriteCommand(content_path))
        self.workspace.write(content_path, stream)

    def commit(self):
        """Commit the transaction (i.e. move assembled object into root."""
        self.repository.storage.move(self.workspace.storage, self.object_path)

    def rollback(self):
        """Rollback the transaction."""
        pass
