#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(
    name='runcurl',
    version='0.4',
    description='A fork of uncurl which includes an execute method to run curl directly.',
    author='Steve Pulec, Halil Ozercan',
    author_email='halilozercan@gmail',
    url='https://github.com/halilozercan/runcurl',
    entry_points={
        'console_scripts': [
            'runcurl = runcurl.bin:main',
        ],
    },
    packages=find_packages(exclude=("tests", "tests.*")),
)
