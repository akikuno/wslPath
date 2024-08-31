import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wslPath",
    version="0.4.2",
    author="Akihiro Kuno",
    author_email="akuno@md.tsukuba.ac.jp",
    description="Python module to convert between Windows and POSIX path",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akikuno/wslPath",
    packages=setuptools.find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
