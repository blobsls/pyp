# File: setup.py
# This script will set up your package for distribution.

from setuptools import setup, find_packages

setup(
    name='pyp_package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyp=pyp_package.cli:main',
        ],
    },
    # Add other metadata like author, description, dependencies, etc.
)
