import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "clippy",
    version = "0.0.1",
    author = "Igor Guerrero",
    author_email = "igfgt1@gmail.com",
    description = ("A copy to clipboard widget for Django."),
    license = "MIT",
    keywords = "django clippy clipboard",
    url = "https://github.com/igorgue/django-clippy",
    include_package_data = True,
    packages=find_packages(),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '*': ['*'],
    },
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.6",
        "License :: OSI Approved :: MIT License",
    ],
)
