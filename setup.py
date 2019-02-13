#!/usr/bin/env python3
"""Home Assistant setup script."""
from datetime import datetime as dt
from setuptools import setup, find_packages
from pytables import const as pytables_const

PROJECT_NAME = 'PyTables'
PROJECT_PACKAGE_NAME = 'pytables'
PROJECT_LICENSE = 'Apache License 2.0'
PROJECT_AUTHOR = 'The PyTables Authors'
PROJECT_COPYRIGHT = ' 2019-{}, {}'.format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://github.com/zabuldon/pytables'
PROJECT_EMAIL = 'vortexius@gmail.com'

PROJECT_GITHUB_USERNAME = 'zabuldon'
PROJECT_GITHUB_REPOSITORY = 'pytables'

PYPI_URL = 'https://pypi.python.org/pypi/{}'.format(PROJECT_PACKAGE_NAME)
GITHUB_PATH = '{}/{}'.format(
    PROJECT_GITHUB_USERNAME, PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = 'https://github.com/{}'.format(GITHUB_PATH)

DOWNLOAD_URL = '{}/archive/{}.zip'.format(GITHUB_URL, pytables_const.__version__)
PROJECT_URLS = {
    'Bug Reports': '{}/issues'.format(GITHUB_URL),
}

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

REQUIRES = [
    'flask',
    'flask-sqlalchemy',
    'flask-bootstrap',
    'flask-login',
    'flask-wtforms',
    'flask-resful',
    'flask-migrate',
    'python-slugify',
    'pyyaml',
    'voluptuous',
]

MIN_PY_VERSION = '.'.join(map(str, pytables_const.REQUIRED_PYTHON_VER))

setup(
    name=PROJECT_PACKAGE_NAME,
    version=pytables_const.__version__,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires='>={}'.format(MIN_PY_VERSION),
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'hass = pytables.__main__:main'
        ]
    },
)