# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""Transaction used for as close as possible for atomic operations.

Transactions works by assembling the OCFL object or OCFL version in a separate
workspace and then transfer it into the OCFL stroage root in as safe manner as
possible. It also keeps a transaction log of commands executed (e.g. writing),
so that in case a commands fails, we can undo executed commands.

The goal of the transaction is to have as close to atomic operations as
possible, but since we're dealing with file systems, we're not gonna have
ACID properties like in a database.
"""


class Command:
    """A transaction command."""

    def undo(self):
        """Undo the command."""
        pass


class WriteCommand(Command):
    """A write command."""

    def __init__(self, path):
        """Constructor."""
        self.path = path

    def undo(self):
        """Undo the command."""
        # TODO
        pass
