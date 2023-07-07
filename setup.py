from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="movingpeople",
    version="0.0.10",
    description="Generate synthetic timesstamped routes on a graph network.",
    package_dir={"": "movingpeople"},
    packages=find_packages(where="movingpeople"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elz1582/movingpeople",
    author="Elliot H",
    author_email="Elliot H",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "bson >= 0.5.10"
        ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "twine>=4.0.2"
            ],
    },
    python_requires=">=3.10",
)