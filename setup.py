import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="Kyan",
    version="1.1.5",
    description="A soundboard program written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoubleF3lix/Kyan/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)