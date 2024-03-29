"""Setup script for EducalingoDictionary"""

import os.path
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="educalingoDictionary",
    version="v0.1.0-alpha",
    description="Gets data from the Educalingo dictionary",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JessicaSousa/EducalingoDictionary",
    project_urls={
        "Documentation": "https://github.com/JessicaSousa/EducalingoDictionary",
        "Source": "https://github.com/JessicaSousa/EducalingoDictionary",
        "Tracker": "https://github.com/JessicaSousa/EducalingoDictionary/issues",
    },
    author="Jessica Sousa",
    author_email="jessicacardosops@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    keywords="scrapping dictionary",
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4"],
    tests_require=["pytest"],
)
