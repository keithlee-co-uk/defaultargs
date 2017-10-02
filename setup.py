#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='defaultargs',
      version='0.0.1',
      description='Python Default Argument Decorators',
      author='Keith Lee',
      author_email='code@keithlee.co.uk',
      url='https://github.com/keithlee-co-uk/defaultargs',
      packages=['defaultargs'],

      install_requires=requirements,
      extras_require={
          'test': ["pytest"],
      }
      )
