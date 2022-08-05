import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="numdoc",
    version="0.0.2",
    author="N.Wen",
    author_email="nwen@clemson.edu",
    description="Serializing, deserializing and hashing documents (JSON) with scientific data types (numpy)",
    long_description="Serializing, deserializing and hashing documents (JSON) with scientific data types (numpy)",
    long_description_content_type="text/markdown",
    url="https://github.com/nwen-cu/numdoc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)