# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name="jukebox-live-indexer",
    packages=find_packages(),
    version="0.1.1",
    description="Background library indexing service for jukebox",
    author="Jens Nistler",
    author_email="opensource@jensnistler.de",
    url="http://jensnistler.de/",
    download_url='http://github.com/lociii/jukebox_live_indexer',
    keywords=["jukebox", "music", "mp3", "background", "library", "indexer"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Players",
    ],
    install_requires=[
        "jukebox>=0.3.7",
        "python-daemon==1.6",
        "watchdog>=0.6.0",
    ],
    include_package_data=True,
    long_description=open("README.rst").read()
)
