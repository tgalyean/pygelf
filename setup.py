#!/usr/bin/env python

from setuptools import setup, find_packages

setup(

    name='pygelf',
    version='0.1',
    description='Python Gelf HTTP libary',
    author='Tim Galyean',
    author_email='tim.galyean@gmail.com',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['pycurl']

)
