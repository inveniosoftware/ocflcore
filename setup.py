# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Data Futures.
#
# OCFL Core is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Oxford Common Filesystem Layout module for Python."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "black>=21.12b0",
    "check-manifest>=0.42",
    "coverage>=5.3,<6",
    "pydocstyle<=6.1.1",
    "pytest-cov>=2.10.1",
    "pytest-isort>=1.2.0",
    "pytest-pycodestyle>=2.2.0",
    "pytest-pydocstyle>=2.2.0",
    "pytest>=6,<7",
]

extras_require = {
    "docs": [
        "Sphinx==4.2.0",
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("ocflcore", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="ocflcore",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="OCFL package for Python.",
    license="MIT",
    author="CERN & Data Futures",
    author_email="info@inveniosoftware.org",
    url="https://github.com/inveniosoftware/ocflcore",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    extras_require=extras_require,
    tests_require=tests_require,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 1 - Planning",
    ],
)
