
from setuptools import setup, find_packages
from pinnacle import __version__

setup(
    name="pinnacle",
    version=__version__,
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Pinnacle API Python wrapper",
    url="https://github.com/rozzac90/pinnacle",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open('README.md').read(),
    tests_require=['pytest'],
)
