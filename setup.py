import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number-theory",
    version="2.4.2",
    author="Ashwin Naren",
    author_email="arihant2math@gmail.com",
    description="A large number theory package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arihant2math/number-theory",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=[
        'statistics',
        'pytest>=5.4.3',
        'packaging>=20.4',
    ],
)
