import os
from setuptools import find_packages, setup

from external_links import __version__

setup(name='django-external-links',
    version=__version__,
    description='A generic application to keep track of the clicks on the external links in your sites',
    author='Jesús Del Carpio',
    author_email='jjdelc@gmail.com',
    url='https://github.com/jjdelc/django-external-links',
    package_dir={'external_links': 'external_links'},
    packages=find_packages(),
    include_package_data=True,
)
