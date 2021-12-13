# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Test of an OCFL Object."""

from io import BytesIO
from os.path import exists, join

from ocflcore import (
    FileSystemStorage,
    OCFLObject,
    OCFLRepository,
    OCFLVersion,
    StorageRoot,
    StreamDigest,
    TopLevelLayout,
)


#
# Tests
#
def test_ocflobject(now):
    example_file = StreamDigest(BytesIO(b"minimal example"))

    v = OCFLVersion(now)
    v.files.add("file.txt", example_file.stream, example_file.digest)

    o = OCFLObject("12345-abcde")
    o.versions.append(v)

    assert o.id == "12345-abcde"
    assert len(o.versions) == 1
    assert len(o.versions[0].files) == 1
    assert o.head == o.versions[0]


def test_repository_init(tmpdir):
    storage = FileSystemStorage(tmpdir.mkdir("root"))
    workspace_storage = FileSystemStorage(tmpdir.mkdir("workspace"))
    root = StorageRoot(TopLevelLayout())
    repository = OCFLRepository(root, storage, workspace_storage)
    repository.initialize()

    assert exists(join(tmpdir, "root/0=ocfl_1.1"))
    assert exists(join(tmpdir, "root/ocfl_layout.json"))
    assert not exists(join(tmpdir, "root/ocfl_1.1.txt"))


def test_repository_add(tmpdir, repository, minimal_obj):
    repository.add(minimal_obj)
    assert exists(join(tmpdir, "root/0=ocfl_1.1"))
    assert exists(join(tmpdir, "root/ocfl_layout.json"))
