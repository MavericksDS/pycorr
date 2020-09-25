# -*- coding: utf-8 -*-


import os
import sys

from pip._internal.req import parse_requirements
from setuptools import find_packages, setup
from setuptools.command.install import install

VERSION = "0.1.5"

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pycorr",
    version=VERSION,
    description="Python package for calculating correlation amongst categorical variables",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Anurag Kumar Mishra",
    author_email="anuragkm25@outlook.com",
    url="https://github.com/MavericksDS/pycorr",
    packages=find_packages(exclude=("tests", "docs")),
    install_reqs=parse_requirements("requirements.txt", session="hack"),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
