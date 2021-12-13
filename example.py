# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Basic example."""

from datetime import datetime, timezone
from io import BytesIO

from invenio_ocfl.records import FileSystemStorage, OCFLRepository
from invenio_ocfl.services import (
    OCFLObject,
    OCFLVersion,
    StorageRoot,
    StreamDigest,
    TopLevelLayout,
)

# Create a minimal OCFL object
# ============================
# In memory file with a computed digest - StreamDigest to be revisted
example_file = StreamDigest(BytesIO(b"minimal example"))
# Create a version
v = OCFLVersion(datetime.now(timezone.utc))
v.files.add("file.txt", example_file.stream, example_file.digest)
# Create the object - id should be a uri ...things to fix
o = OCFLObject("12345-abcde")
o.versions.append(v)

# Setup root
# ==========
root = StorageRoot(TopLevelLayout())

# Setup repository
# ================
# ATTENTION: Will create root/workspace directors in current working directory.
storage = FileSystemStorage("root")
workspace_storage = FileSystemStorage("workspace")

repository = OCFLRepository(root, storage, workspace_storage=workspace_storage)
repository.initialize()

# Add object to repository
# ========================
repository.add(o)
