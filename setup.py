# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CrunchbaseAPIExtract',
    version='0.1.0',
    description='Extract data from Crunchbase API and upload to AWS S3',
    long_description=readme,
    author='Robele Baker',
    author_email='robele@hubilo.com',
    url='https://github.com/hubilo/CrunchbaseAPIExtract',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

