#!/usr/bin/env python3
"""Setup file for the openSenseMap API Python client."""
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="opensensemap-api",
    version="0.3.2",
    description="Python client for interacting with the openSenseMap API.",
    long_description=long_description,
    url="https://github.com/home-assistant-ecosystem/python-opensensemap-api",
    download_url="https://github.com/home-assistant-ecosystem/python-opensensemap-api/releases",
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    license="MIT",
    install_requires=[
        "aiohttp>=3.8.5,<4",
        "async_timeout>=4,<5",
    ],
    packages=["opensensemap_api"],
    zip_safe=True,
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
)
