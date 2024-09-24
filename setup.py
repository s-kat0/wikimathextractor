import re

from setuptools import find_packages, setup

from wikimathextractor.WikiMathExtractor import __version__


def get_version(version):
    if re.match(r"^\d+\.\d+$", version):
        return version + ".0"
    return version


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wikimathextractor",
    version=get_version(__version__),
    author="Shota Kato",
    author_email="shota@human.sys.i.kyoto-u.ac.jp",
    description="A tool for extracting plain text and mathematical formulas from Wikipedia dumps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU Affero General Public License",
    install_requires=[],
    url="https://github.com/stktu/wikimathextractor",
    packages=find_packages(include=["wikimathextractor"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "wikimathextractor = wikimathextractor.WikiMathExtractor:main",
            "extractPage = wikimathextractor.extractPage:main",
        ]
    },
    python_requires=">=3.6",
)
