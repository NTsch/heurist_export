from setuptools import setup, find_packages

setup(
    name='heurist2ediarum',
    version='0.1',
    author='Niklas',
    description='Connects Ediarum to Heurist DB automatically.',
    packages=find_packages(),
    install_requires=[
        'Flask',
        # Other dependencies
    ],
)