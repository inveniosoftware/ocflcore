..
    Copyright (C) 2021 CERN.

    OCFL Core is free software; you can redistribute it and/or modify it under
    the terms of the MIT License; see LICENSE file for more details.

===========
 OCFL Core
===========

.. image:: https://github.com/inveniosoftware/ocflcore/workflows/CI/badge.svg
        :target: https://github.com/inveniosoftware/ocflcore/actions?query=workflow%3ACI

.. image:: https://img.shields.io/github/tag/inveniosoftware/ocflcore.svg
        :target: https://github.com/inveniosoftware/ocflcore/releases

.. image:: https://img.shields.io/pypi/dm/ocflcore.svg
        :target: https://pypi.python.org/pypi/ocflcore

.. image:: https://img.shields.io/github/license/inveniosoftware/ocflcore.svg
        :target: https://github.com/inveniosoftware/ocflcore/blob/master/LICENSE

OCFL Core is a Python library for working with
[Oxford Common Filesystem Layout](https://ocfl.io).

Features include:

- Domain model API: Implements a flexible domain model API for working with
  OCFL, that allows easy customization of OCFL features such as e.g. storage
  hierarchies.
- Storage abstraction: Works with byte streams to allow any storage system to
  be used.
- Deduplication: Content files are automatically deduplicated in the OCFL
  object.
- Segregating Objects-in-flight: A workspace is being used to assemble objects
  prior to adding them into the repository to ensure as atomic operations as
  possible on top of a file system and with support for cleaning up after
  failed operations.

Further documentation is available on https://ocflcore.readthedocs.io/.

Quick start
-----------

Import the required classes:

.. code-block:: python

    from datetime import datetime, timezone
    from io import BytesIO

    from ocflcore import (
        FileSystemStorage,
        OCFLRepository,
        OCFLObject,
        OCFLVersion,
        StorageRoot,
        StreamDigest,
        TopLevelLayout,
    )


Create a OCFL storage root using  a top-level storage hierarchy:

.. code-block:: python

    root = StorageRoot(TopLevelLayout())


Initialize an OCFL repository:

.. code-block:: python

    # Setup workspace and root storage:
    storage = FileSystemStorage("root")
    workspace_storage = FileSystemStorage("workspace")
    # Initialize the repository
    repository = OCFLRepository(root, storage, workspace_storage=workspace_storage)
    repository.initialize()


Create an in-memory example file and compute its SHA512 digest:

.. code-block:: python

    example_file = StreamDigest(BytesIO(b"minimal example"))


Create a minimal OCFL object:

.. code-block:: python

    # Create version
    v = OCFLVersion(datetime.now(timezone.utc))
    v.files.add("file.txt", example_file.stream, example_file.digest)

    # Create the object
    o = OCFLObject("12345-abcde")
    o.versions.append(v)

Last, but not least, add the OCFL object to the OCFL repository:

.. code-block:: python

    repository.add(o)

**Result**

The result is an OCFL repository:

.. code-block:: console

    $ tree .
    .
    |-- root
    |   |-- 0=ocfl_1.1
    |   |-- 12345-abcde
    |   |   |-- 0=ocfl_object_1.1
    |   |   |-- inventory.json
    |   |   |-- inventory.json.SHA512
    |   |   `-- v1
    |   |       |-- content
    |   |       |   `-- file.txt
    |   |       |-- inventory.json
    |   |       `-- inventory.json.SHA512
    |   `-- ocfl_layout.json
    `-- workspace

    5 directories, 8 files

With the OCFL inventories and nameste files:


.. code-block:: console

    $ cat root/12345-abcde/inventory.json
    {
    "contentDirectory": "content",
    "digestAlgorithm": "sha512",
    "head": "v1",
    "id": "12345-abcde",
    "manifest": {
        "8ef7dc319954f0d8ed13b1da8e744a4e00fad3cf0952a9ee75c51f455769f1b7c09d623b3ec433483d2627b85100485727a4f200a7b75fb7f81a41af451167da": [
        "v1/content/file.txt"
        ]
    },
    "type": "https://ocfl.io/1.1/spec/#inventory",
    "versions": {
        "v1": {
        "created": "2021-12-14T08:09:17.743663+00:00",
        "state": {
            "8ef7dc319954f0d8ed13b1da8e744a4e00fad3cf0952a9ee75c51f455769f1b7c09d623b3ec433483d2627b85100485727a4f200a7b75fb7f81a41af451167da": [
            "file.txt"
            ]
        }
        }
    }
    }

Install
-------

.. code-block:: console

    pip install ocflcore


Running tests
-------------

.. code-block:: console

    git clone https://github.com/inveniosoftware/ocflcore
    cd ocflcore
    pip install -e ".[all]"
    ./run-tests.sh

