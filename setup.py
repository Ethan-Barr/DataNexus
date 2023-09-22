from setuptools import setup, find_packages

setup(
    name='datanest',
    version='0.0.2',
    description='A dataset module for your projects',
    author='Ethan Barr',
    author_email='ethanwbarr07@gmail.com',
    url='https://github.com/Ethan-Barr/Datanest',
    packages=find_packages(),
    install_requires=[
    "Requests==2.28.2"
    ],
)
