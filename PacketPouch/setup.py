from setuptools import setup, find_packages

setup(
    name="PacketPouch",
    version="1.0.0",
    author="Lucas",
    author_email="luquinhasdesouza2018@gmail.com",  
    description="Fun Python library for file handling and networking",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://example.com/",  
    packages=find_packages(),
    python_requires=">=3.10", 
    install_requires=[
        #nothing
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
