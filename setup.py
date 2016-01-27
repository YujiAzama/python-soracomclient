import os
from setuptools import find_packages
from setuptools import setup

setup(
    name = "python-soracomclient",
    author = "Yuji Azama",
    author_email = "yuji.azama@gmail.com",
    license = "Apache License, Version 2.0",
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7"
    ],
)
