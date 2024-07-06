from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-readme-stats",
    version="0.1.1",
    author="Dubasi Pavan Kumar",
    author_email="pavan.dubasi2024@gmail.com",
    description="Automatically update your GitHub README with your latest GitHub statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ascender1729/github-readme-stats",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyGithub>=1.55",
        "python-dotenv>=0.19.0",
    ],
)