import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="Kyan",
    version="1.0.1",
    description="A soundboard program written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoubleF3lix/Kyan/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3.0",
        "Operating System :: Windows 10",
    ]
)