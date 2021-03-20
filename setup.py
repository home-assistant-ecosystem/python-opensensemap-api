#!/usr/bin/env python3
"""Setup file for the openSenseMap API Python client."""
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="opensensemap-api",
    version="0.1.5",
    description="Python client for interacting with the openSenseMap API.",
    long_description=long_description,
    url="https://github.com/home-assistant-ecosystem/python-opensensemap-api",
    download_url="https://github.com/home-assistant-ecosystem/python-opensensemap-api/releases",
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    license="MIT",
    install_requires=["aiohttp>=3.7.4,<4", "async_timeout<4"],
    packages=["opensensemap_api"],
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
    ],
)
