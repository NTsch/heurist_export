from setuptools import setup, find_packages

setup(
    name='Heurist2Ediarum',
    version='0.1',
    author='Niklas',
    description='Connects Ediarum to Heurist DB automatically.',
    packages=find_packages(),
    install_requires=[
        'Flask',
        # Other dependencies
    ],
)