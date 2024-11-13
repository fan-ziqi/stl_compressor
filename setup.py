from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="stl_compressor",
    version="2.2",
    description="STL Compressor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ziqi Fan",
    author_email="fanziqi614@gmail.com",
    url="https://github.com/fan-ziqi/stl_compressor",
    install_requires=[],
    license="Apache License 2.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["stl_compressor = stl_compressor.stl_compressor_ui:main"]},
    platforms=["all"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
