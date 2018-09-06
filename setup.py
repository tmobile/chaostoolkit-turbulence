#!/usr/bin/env python
"""chaostoolkit turbulence extension builder and installer"""

import sys
import io

from setuptools import setup

sys.path.insert(0, ".")
from chaosturbulence import __version__
sys.path.remove(".")

name = 'chaostoolkit-turbulence'
desc = 'Chaos Toolkit Turbulence support'

with io.open('README.md', encoding='utf-8') as strm:
    long_desc = strm.read()

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation'
]
author = 'Matthew Conover'
author_email = 'matthew.conover1@t-mobile.com'
url = 'http://chaostoolkit.org'
packages = [ 'chaosturbulence' ]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]


def main():
    """Package installation entry point."""
    setup(
        name=name,
        version=__version__,
        description=desc,
        long_description=long_desc,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        url=url,
        packages=packages,
        include_package_data=True,
        install_requires=install_require,
        python_requires='>=3.5.*'
    )


if __name__ == '__main__':
    main()
