#!/usr/bin/env python

from distutils.core import setup

setup(name='compfi',
      version='0.1',
      description='commandline tool for compound.finance',
      url='https://github.com/donpdonp/compfi/',
      packages=['compfi'],
      entry_points={
        "console_scripts": [
            "compfi=compfi:patched_main",]},
     )
