# File: setup.py
# This script will set up your package for distribution.

from setuptools import setup, find_packages
import pip
import wheel

setup(
    name='pyp_package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyp=pyp_package.cli:main',
        ],
    },
    install_requires={
        pip>=25.0,
        setup>=68.0,
        wheel>=0.33,
        
    }
)
