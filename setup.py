#!/usr/bin/env python

from distutils.core import setup

setup(
    name='csvrewrite',
    version='1.0.0',
    description='Script to convert between CSV, TSV, and similar formats',
    long_description=open('README.md').read(),
    author='Benjamin Hottell',
    author_email='benjaminhottell@gmail.com',
    url='https://github.com/benjaminhottell/pycsvrewrite',
    license='AGPL',
    scripts=['csvrewrite'],
    packages=[]
)

