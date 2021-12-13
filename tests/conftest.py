# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration."""

from datetime import datetime, timezone
from io import BytesIO

import pytest

from ocflcore import (
    FileSystemStorage,
    OCFLObject,
    OCFLRepository,
    OCFLVersion,
    StorageRoot,
    StreamDigest,
    TopLevelLayout,
)


@pytest.fixture()
def repository(tmpdir):
    """Repository fixture."""
    storage = FileSystemStorage(tmpdir.mkdir("root"))
    workspace_storage = FileSystemStorage(tmpdir.mkdir("workspace"))
    root = StorageRoot(TopLevelLayout())
    repository = OCFLRepository(root, storage, workspace_storage=workspace_storage)
    repository.initialize()
    return repository


@pytest.fixture()
def minimal_obj(now):
    """Minimal OCFL object."""
    example_file = StreamDigest(BytesIO(b"minimal example"))
    v = OCFLVersion(now)
    v.files.add("file.txt", example_file.stream, example_file.digest)

    o = OCFLObject("12345-abcde")
    o.versions.append(v)
    return o


@pytest.fixture()
def now():
    """Timezone-aware UTC timestamp."""
    return datetime.now(timezone.utc)
