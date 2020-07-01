import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number-theory",
    version="1.2",
    author="Ashwin Naren",
    author_email="arihant2math@gmail.com",
    description="A large number theory package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arihant2math/number-theory/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
