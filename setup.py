from distutils.core import setup

from setuptools import find_packages

setup(
    name='minecraft-data',
    description='Provide easy access to minecraft-data in python',
    license='MIT',
    long_description=open('README.rst').read(),
    version='0.0.1',
    url='https://github.com/rom1504/python-minecraft-data',
    packages=find_packages(),
    install_requires=[
    ],
    keywords=['minecraft'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)