# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "swagger-ui-bundle==0.0.6",
    "connexion==2.6.0",
    "elasticsearch==7.6",
    "python_dateutil==2.6.0",
    "Flask-Testing >= 0.8.0"
    ]

setup(
    name=NAME,
    version=VERSION,
    description="Orphadata API",
    author_email="data.orphanet@inserm.fr",
    url="",
    keywords=["Swagger", "Orphadata API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.API_main:main']},
    long_description="""\
    Orphadata provides APIs for the scientific community with comprehensive, quality data sets related to rare diseases and orphan drugs from the Orphanet knowledge base.
    """
)
