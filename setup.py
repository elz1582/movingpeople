from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="example_app",
    version="0.0.10",
    description="A basic tempalte",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="Elliot",
    author_email="Elliot",
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