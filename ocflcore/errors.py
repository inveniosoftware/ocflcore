# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

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
