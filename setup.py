#!/usr/bin/env python

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

from miniodm import __version__

SETTINGS = {'name': 'miniodm',
            'version': __version__,
            'description': 'A minimalist ODM for Python and MongoDB',
            'url': 'http://github.com/indienick/miniodm',
            'download_url': 'http://cloud.github.com/downloads/indienick/miniodm/miniodm-{0}.tar.gz'.format(__version__),
            'author': 'Nick Saika',
            'author_email': 'nicksaika@gmail.com',
            'maintainer': 'Nick Saika',
            'maintainer_email': 'nicksaika@gmail.com',
            'keywords': ['mongodb', 'odm'],
            'license': 'BSD',
            'packages': ['miniodm'],
}

setup(**SETTINGS)
