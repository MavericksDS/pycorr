# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pip.req import parse_requirements

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pycorrcat',
    version='0.1.0',
    description='Python package for calculating correlation amongst categorical variables',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Anurag Kumar Mishra',
    author_email='anuragkm25@outlook.com',
    url='https://github.com/MavericksDS/pycorrcat',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_reqs = parse_requirements('requirements.txt', session='hack'),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)