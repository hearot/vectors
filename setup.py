#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vectors',
    version='1.0.0',
    description='A simple library for vectors in Python 3.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hearot/vectors',
    author='Hearot',
    author_email='gabriel@hearot.it',
    packages=['vectors'],
    python_requires='>=3.5',
    install_requires=['sympy'],
)
