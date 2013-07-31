#!/usr/bin/env python

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

from pureodm import __version__

SETTINGS = {
    'name': 'pureodm',
    'version': __version__,
    'description': 'A minimalist ODM for Python and MongoDB',
    'url': 'http://indienick.github.com/pureodm',
    'download_url': 'https://github.com/indienick/pureodm/tarball/{0}'.format(__version__),
    'author': 'Nick Saika',
    'author_email': 'nicksaika@gmail.com',
    'maintainer': 'Nick Saika',
    'maintainer_email': 'nicksaika@gmail.com',
    'keywords': ['mongodb', 'odm'],
    'license': 'BSD',
    'packages': ['pureodm'],
    'install_requires': ['pymongo>=2.4.1'],
}

setup(**SETTINGS)
