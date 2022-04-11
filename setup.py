from setuptools import setup, find_packages

long_description = 'A light-weight library which does not require any libraries to install and processes data from pandas, numpy or a normal python array.'

setup(
    name='technical_analysis',
    description=long_description,
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
        ],

)
