import os
from setuptools import setup

# Utility function to read the README file.

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyPiCount", # this is the name of the package
    version = "0.1.0", # the initial release version
    author = "Adriana Solis, Alexis Caldwell, Rachael Harris, Ramon Guzman, Ryan Hilty", # author names
    author_email = "solisa@allegheny.edu, caldwella2@allegheny.edu, harrisr@allegheny.edu, guzmanr@allegheny.edu, hiltyr@allegheny.edu",
    description = ("A python program to count the number of instances of different specifications."),
    license = "MIT",
    keywords = "python counter",
    url = "https://github.com/cmpsc-481-s22-m1/PyCount",
    packages=['PyCount', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Education :: Testing",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
)
