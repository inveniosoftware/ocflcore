# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""OCFL Repository.

Layer that mediates between the domain layer and the low-level implementation.
The repository uses the concept of a transaction to write objects into the OCFL
storage root by first writing objects to a workspace and later transfer them
to the root as described in the OCFL Implementation Notes.
"""

from io import BytesIO

from .inventory import Inventory, InventoryContent
from .transaction import Transaction


class OCFLRepository:
    """Repository for OCFL objects.

    The repository takes care of reading and writing of OCFL objects in the
    OCFL storage root, as well as handling updates.

    The class is named repository after the repository pattern in
    "Fowler (2002). Patterns of Enterprise Application Architecture".
    """

    def __init__(self, root, storage, workspace_storage=None):
        """Constrcutor."""
        self.root = root
        self.storage = storage
        self.workspace_storage = workspace_storage

    def initialize(self):
        """Initialize OCFL repository."""
        # Write root conformace declaration - See 4.2
        self.storage.write(self.root.namaste, BytesIO(b""))
        # Write optional human readable text - See 4.1
        if self.root.human_text is not None:
            self.storage.write(
                self.root.human_text_filename, BytesIO(self.root.human_text)
            )
        # Write optional layout file - See 4.1
        layout_json = self.root.layout.json_bytes
        if layout_json is not None:
            self.storage.write("ocfl_layout.json", BytesIO(layout_json))

    def add(self, obj):
        """Add an OCFL object to the storage root."""
        with Transaction(self, obj) as t:
            inventory = Inventory(obj)
            # Write object conformace declaration - see 3.2
            t.write(inventory.nameste, BytesIO(b""))
            # Write content files - see 3.3
            for content_path, f in obj.content_files():
                t.write(content_path, f.stream)
            # Write main inventory - see 3.5 and 3.6
            content = InventoryContent(inventory)
            t.write(content.name, BytesIO(content.bytes))
            t.write(content.sidecar_name, BytesIO(content.sidecar_bytes))
            # Write version inventories (optional - see 3.7)
            for version_number in obj.version_numbers:
                content = InventoryContent(Inventory(obj, version=version_number))
                t.write(f"v{version_number}/{content.name}", BytesIO(content.bytes))
                t.write(
                    f"v{version_number}/{content.sidecar_name}",
                    BytesIO(content.sidecar_bytes),
                )
            # Move/copy to storage root
            t.commit()

    def add_version(self, obj_id, version):
        """Add new version to an OCFL object."""
        # TODO
        pass

    def get(self, obj_id):
        """Get an OCFL object from the storage root."""
        # TODO
        pass

    def list(self):
        """List objects in an OCFL object root."""
        # TODO
        pass
