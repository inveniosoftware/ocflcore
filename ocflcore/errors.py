# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-FileCopyrightText: 2021 Data Futures.
# SPDX-License-Identifier: MIT

"""Errors for OCFL Core."""


class OCFLException(Exception):
    """Base class for all OCFL exceptions."""

    pass


class ConstraintException(OCFLException):
    """Base for constraint errors.."""

    pass


class LogicalPathError(ConstraintException):
    """An error related to a logical path."""

    pass


class ObjectNotFoundError(OCFLException):
    """Specified object does not exist."""

    pass


class OCFLFileNotFoundError(OCFLException):
    """Specifed file does not exist."""

    pass
