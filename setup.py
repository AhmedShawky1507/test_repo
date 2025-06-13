#!/usr/bin/env python3
from setuptools import setup

# Absolute minimum configuration
setup(
    name="your_project",  # Required
    version="0.1.0",     # Required
    packages=[""],       # Packages to include (empty string = current directory)
    
    # Critical for Kali Linux compatibility:
    python_requires=">=3.6",
    setup_requires=["setuptools==68.2.0", "jaraco.functools==4.0.0"],
)
print("Hello world!!!!!!!!!!!!!!!!!!!!!")
