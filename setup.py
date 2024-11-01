# setup.py
from setuptools import setup, find_packages

setup(
    name='ml_loader',
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
    author='Sazib',
    author_email='sazibc5@gmail.com',
    url='https://github.com/sazib0/ml_loader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)