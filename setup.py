#!/usr/bin/env python

from setuptools import setup, find_packages

setup(

    name='pygelf',
    version='0.1',
    description='Python library for sending events to Graylog2 over the Gelf HTTP Input',
    author='Tim Galyean',
    author_email='tim.galyean@gmail.com',
    license='GPL V2',
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['pycurl']

)
