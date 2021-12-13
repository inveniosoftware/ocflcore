# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Factory of OCFL objects."""

# TODO: Should probably be moved to Invenio.


class OCFLBuilder:
    """OCFL builder."""

    def __init__(self):
        """Constructor."""
        # ...
        pass

    def build_version(obj, record):
        """Build a version."""
        obj.version

    def build(record):
        """Build an object."""
        data = serializer.serialize(record)
        for path, serializer in serializers:
            obj.add_file(path, data, fixity="")


# record_builder = RDMRecordOCFLBuilder(
#     record_serializers={
#         'datacite.json': DataCite43JSONSerializer(),
#         'marc21.xml': MARC21Seria lizer(),
#         'dublin-core.xml': DublinCoreSerializer(),
#     }
#     files_serializers={
#         'datacite.json': FileSerializer(),
#     }
# )
# parent_builder = RDMParentOCFLBuilder()

# ocfl_obj = builder.build_object(record)
# ocfl_obj = builder.build_object(parent)
