# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Logical representation of an OCFL Object."""

from ..errors import LogicalPathError


#
# Validators
#
def validate_fixity_algo(algo):
    """Validate accepted digest algorithms."""
    assert algo in ["md5", "sha1", "sha256", "sha512", "blake2b-512"]


def validate_digest_algo(algo):
    """Validate accepted digest algorithms."""
    assert algo in ["sha256", "sha512"]


def validate_spec(spec):
    """Validate a version for the OCFL spec."""
    assert spec in ["1.0", "1.1"]


def validate_path(path):
    """Validate a path according to OCFL."""
    # See 3.5.3.1
    assert path[0] != "/"
    assert path[-1] != "/"
    for path_elem in path.split("/"):
        validate_path_elem(path_elem)


def validate_path_elem(path_elem):
    """Validate a path element according to OCFL."""
    # See 3.5.3.1
    assert "/" not in path_elem
    assert path_elem not in ["", ".", ".."]


#
# Logical files for a version
#
class VersionFile:
    """Represents a file associated with a version."""

    def __init__(self, logical_path, stream, digest, fixity=None):
        """Constructor for a file."""
        self._logical_path = logical_path
        self._stream = stream
        self._digest = digest
        self._fixity = fixity

    @property
    def digest(self):
        """The logical path inside the version."""
        return self._digest

    @property
    def stream(self):
        """The logical path inside the version."""
        return self._stream

    @property
    def fixity(self):
        """The logical path inside the version."""
        return self._fixity

    @property
    def logical_path(self):
        """The logical path inside the version."""
        return self._logical_path

    def content_path(self, idx, content_directory):
        """Generate a content path for this file relative to object root."""
        return f"v{idx}/{content_directory}/{self.logical_path}"


class FilesManager:
    """Files manager for an OCFL version."""

    def __init__(self, inventory=None):
        """Constructor."""
        self._files = {}

    def __len__(self):
        """Number of versions."""
        return len(self._files)

    def __iter__(self):
        """Iterator over the files."""
        for f in self._files.values():
            yield f

    def add(self, logical_path, stream, digest, fixity=None):
        """Add a new file to the version."""
        if logical_path in self._files:
            raise LogicalPathError("Logical path already present in version.")
        validate_path(logical_path)
        self._files[logical_path] = VersionFile(
            logical_path, stream, digest, fixity=fixity
        )


#
# Versions
#
class OCFLVersion:
    """Logical representation of a version."""

    def __init__(self, creation_time):
        """Constructor."""
        self._created = creation_time
        self._files = FilesManager()
        self._version_index = None
        self._user = None
        self._message = None

    @property
    def index(self):
        """Get the version index."""
        return self._version_index

    @property
    def files(self):
        """Get the object identifier."""
        return self._files

    @property
    def created(self):
        """Creation date."""
        return self._created

    @property
    def message(self):
        """Get the message."""
        return self._message

    @property
    def user(self):
        """Get the message."""
        return self._user

    @property
    def state(self):
        """Version state."""
        result = {}
        for f in self.files:
            if f.digest not in result:
                result[f.digest] = []
            result[f.digest].append(f.logical_path)
        return result


class VersionManager:
    """Version manager for OCFL objects."""

    def __init__(self):
        """Constructor for a version manager."""
        self._versions = []

    def append(self, version):
        """Add a version to the version manager."""
        self._versions.append(version)

    def __len__(self):
        """Number of versions."""
        return len(self._versions)

    def __getitem__(self, index):
        """Number of versions."""
        return self._versions[index]

    def __iter__(self):
        """Iterate the versions."""
        for v in self._versions:
            yield v

    def enumerated(self, version=None):
        """Iterate the versions."""
        # OCFL is 1-indexed.
        for idx, v in enumerate(self._versions):
            version_number = idx + 1
            if version is not None and version == version_number + 1:
                break
            yield version_number, v


#
# OCFL object
#
class OCFLObject:
    """Logical representation of an OCFL Object."""

    def __init__(
        self,
        object_id,
        content_directory="content",
        digest_algorithm="sha512",
        spec="1.1",
    ):
        """OCFL Object constructor."""
        validate_path_elem(content_directory)
        validate_digest_algo(digest_algorithm)
        validate_spec(spec)
        # TODO validate object_id
        self._object_id = object_id
        self._versions = VersionManager()
        self._content_directory = content_directory
        self._digest_algorithm = digest_algorithm
        self._spec = "1.1"

    @property
    def id(self):
        """Get the object identifier."""
        return self._object_id

    @property
    def versions(self):
        """Get the object identifier."""
        return self._versions

    @property
    def version_numbers(self):
        """Return a range of version numbers."""
        return range(1, len(self.versions) + 1)

    @property
    def head(self):
        """Get the most recent version."""
        return self._versions[-1]

    @property
    def content_directory(self):
        """Get the content directory."""
        return self._content_directory

    @property
    def digest_algorithm(self):
        """Get the digest algorithm."""
        return self._digest_algorithm

    @property
    def spec(self):
        """Get OCFL specification for this object."""
        return self._spec

    def content_files(self, version=None):
        """Iterate over deduplicated list of content files."""
        _manifest = {}
        for idx, v in self.versions.enumerated(version=version):
            for f in v.files:
                if f.digest not in _manifest:
                    _manifest[f.digest] = True
                    content_path = f.content_path(idx, self._content_directory)
                    yield (content_path, f)
