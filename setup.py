# setup.py
from setuptools import setup, find_packages

setup(
    name='my_loader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyreadstat',
        'pillow',
        'sqlalchemy',
        'lxml'
    ],
    description='A package to load data files based on their file extension.',
)
