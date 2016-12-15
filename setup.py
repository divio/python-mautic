#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from mautic import __version__


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests-oauthlib',
]

test_requirements = []

setup(
    name='mautic',
    version=__version__,
    description='Python wrapper for Mautic API',
    long_description=readme + '\n\n' + history,
    author='Divio AG',
    author_email='info@divio.com',
    url='https://github.com/divio/python-mautic',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license='LICENSE',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
