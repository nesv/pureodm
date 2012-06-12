#!/usr/bin/env python

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

from pureodm import __version__

SETTINGS = {'name': 'pureodm',
            'version': __version__,
            'description': 'A minimalist ODM for Python and MongoDB',
            'url': 'http://github.com/indienick/pureodm',
            'download_url': 'http://cloud.github.com/downloads/indienick/pureodm/miniodm-{0}.tar.gz'.format(__version__),
            'author': 'Nick Saika',
            'author_email': 'nicksaika@gmail.com',
            'maintainer': 'Nick Saika',
            'maintainer_email': 'nicksaika@gmail.com',
            'keywords': ['mongodb', 'odm'],
            'license': 'BSD',
            'packages': ['pureodm'],
            'install_requires': ['bson>=0.3.3'],
}

setup(**SETTINGS)
