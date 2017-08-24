# coding: utf-8

"""
    See README.md for details
"""


import sys
from setuptools import setup, find_packages

NAME = "nifi-python-swagger-client"
VERSION = "1.0.0"

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger 2.0 client in python for Apache NiFi Rest API",
    author_email="chaffelson@gmail.com",
    url="https://nifi.apache.org/",
    keywords=["Swagger", "NiFi Rest Api", "Python"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and stop 
    processors, monitor queues, query provenance data, and more. Each endpoint below includes a description, 
    definitions of the expected input and output, potential response codes, and the authorizations required to invoke 
    each service.
    """
)
