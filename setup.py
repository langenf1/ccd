#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'ccd'
DESCRIPTION = 'CCD - Cyclic Coordinate Descent'
URL = '...'
EMAIL = 'fabian.langenbach@hva.nl'
AUTHOR = 'Fabian Langenbach'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '1.0.0'

# List of required packages
REQUIRED = [
    'numpy~=1.19.1',
    'matplotlib~=3.3.1'
]

# Optional packages
EXTRAS = {
    # None
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
)
