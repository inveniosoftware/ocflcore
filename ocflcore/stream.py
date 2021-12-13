# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""IO stream utilities."""

import hashlib


class StreamDigest:
    """Utility class for read a stream and computing a digest.

    The stream must support random seek.
    """

    def __init__(self, stream, algo="sha512"):
        """Constructor."""
        self.stream = stream
        self._digest = None
        assert algo in ["sha512", "sha256"]
        self._algo = algo

    @property
    def digest(self):
        """Compute the digest and set seek stream back to beginning."""
        if self._digest is None:
            chunksize = 1024 * 1024
            h = hashlib.new(self._algo)

            while 1:
                chunk = self.stream.read(chunksize)
                if not chunk:
                    break
                h.update(chunk)
            self.stream.seek(0)
            self._digest = h.hexdigest()

        return self._digest
