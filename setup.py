from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'A module all about fruits!'
LONG_DESCRIPTION = 'fruity.py offers everything you need to know about researching fruits!'

# Setting up
setup(
    name="fruity",
    version=VERSION,
    author="mangoess",
    author_email="<adamtamers@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'fruit', 'fruits'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows :: Windows 10",    
        "Programming Language :: Python :: 3",
    ]
)

