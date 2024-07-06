"""Setup file for GitHub README Stats package."""

import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="github-readme-stats",
    version="0.1.0",
    description="A package to update GitHub README with user stats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ascender1729/github-readme-stats",
    author="Dubasi Pavan Kumar",
    author_email="pavan.dubasi2024@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "PyGithub>=1.55",
        "python-dotenv>=0.19.0"
    ],
    entry_points={
        "console_scripts": [
            "github-readme-stats=github_readme_stats.__main__:main",
        ]
    },
)