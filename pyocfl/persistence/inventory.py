# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# PyOCFL is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Inventory for an OCFL object."""

import hashlib
import json


class Inventory:
    """Inventory for an OCFL object."""

    def __init__(self, obj, version=None):
        """Constructor.

        :param obj: An OCFL object.
        :param version: The version number of the object to generate the
            inventory for (optional). Defaults to most recent version.
        """
        self._obj = obj
        self._version = version

    #
    # Inventory properties
    #
    @property
    def id(self):
        """Get the object identifier."""
        return self._obj.id

    @property
    def nameste(self):
        """Get the name-as-text type."""
        return f"0=ocfl_object_{self._obj.spec}"

    @property
    def type(self):
        """Get the object identifier."""
        return f"https://ocfl.io/{self._obj.spec}/spec/#inventory"

    @property
    def digestAlgorithm(self):
        """Get the object identifier."""
        return self._obj.digest_algorithm

    @property
    def head(self):
        """Get version directory name of highest version number."""
        if self._version is None:
            version = len(self._obj.versions)
        else:
            version = self._version
        return f"v{version}"

    @property
    def contentDirectory(self):
        """Get the content directory."""
        return self._obj.content_directory

    @property
    def manifest(self):
        """Get the manifest section."""
        _manifest = {}
        for content_path, f in self._obj.content_files(version=self._version):
            _manifest[f.digest] = [content_path]
        return _manifest

    @property
    def fixity(self):
        """Get the fixity section."""
        _fixity = {}
        for content_path, f in self._obj.content_files(version=self._version):
            if not f.fixity:
                continue
            for algo, digest in f.fixity:
                if algo not in _fixity:
                    _fixity[algo] = {}
                if digest not in _fixity[algo]:
                    _fixity[algo][digest] = []
                _fixity[algo][digest].append(content_path)
        return _fixity

    @property
    def versions(self):
        """Get the versions section."""
        _versions = {}
        for idx, v in self._obj.versions.enumerated(version=self._version):
            version_string = f"v{idx}"
            _versions[version_string] = {
                "created": v.created.isoformat(),
                "state": v.state,
            }
            if v.message:
                _versions[version_string]["message"] = v.message
            if v.user:
                _versions[version_string]["user"] = v.user
        return _versions

    #
    # Serialization
    #
    def to_dict(self):
        """Full representation of the inventory."""
        return {
            "id": self.id,
            "type": self.type,
            "digestAlgorithm": self.digestAlgorithm,
            "head": self.head,
            "contentDirectory": self.contentDirectory,
            "manifest": self.manifest,
            "versions": self.versions,
            "fixity": self.fixity,
        }

    @property
    def json(self):
        """JSON serialization of the inventory."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True).encode("utf8")


class InventoryContent:
    """Serialized content of an inventory with sidecar file."""

    def __init__(self, inventory):
        """Constructor."""
        self._inventory = inventory
        self._bytes = None

    @property
    def digest(self):
        """Digest of the inventory."""
        h = hashlib.new(self._inventory.digestAlgorithm)
        h.update(self.bytes)
        return h.hexdigest()

    @property
    def name(self):
        """File name."""
        return "inventory.json"

    @property
    def path(self):
        """File name."""
        return "inventory.json"

    @property
    def bytes(self):
        """Inventory content as bytes."""
        if self._bytes is None:
            self._bytes = self._inventory.json
        return self._bytes

    @property
    def sidecar_bytes(self):
        """Sidecar file content."""
        return f"{self.digest} inventory.json".encode("utf8")

    @property
    def sidecar_name(self):
        """Get the name of the side car file."""
        return f"inventory.json.{self._inventory.digestAlgorithm.upper()}"
