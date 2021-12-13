# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Logical representation of an OCFL storage root."""


class StorageRoot:
    """OCFL storage root representation."""

    def __init__(self, layout, version="1.1"):
        """Constructor."""
        self.layout = layout
        self.version = version

    @property
    def human_text(self):
        """Human readable text of the OCFL spec."""
        # See 4.2
        # TODO: load using pkg_resources and distribute in package.
        return None

    @property
    def human_text_filename(self):
        """Filename of the OCFL spec."""
        # See 4.2
        return f"ocfl_{self.version}.txt"

    @property
    def namaste(self):
        """Name as text filename for this storage root."""
        return f"0=ocfl_{self.version}"
