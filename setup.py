#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests-oauthlib==0.7.0',
]

test_requirements = []

setup(
    name='python_mautic',
    version='0.1.0',
    description="Python wrapper for Mautic API",
    long_description=readme + '\n\n' + history,
    author="Steelkiwi",
    author_email='hello@steelkiwi.com',
    url='https://github.com/divio/python-mautic',
    packages=[
        'python_mautic',
    ],
    package_dir={'python_mautic':
                 'python_mautic'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_mautic',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
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
