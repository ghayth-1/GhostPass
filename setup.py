"""Setup configuration for GhostPass."""

from setuptools import setup, find_packages

setup(
    name="ghostpass",
    version="1.0.0",
    author="ghayth-1I",
    description="A secure command-line password leak checker powered by Have I Been Pwned.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ghayth-1I/GhostPass",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "colorama>=0.4.6",
    ],
    # ---------------------------------------------------------------
    # THIS is the key part — it creates the `ghostpass` command
    # that you can run from anywhere in your terminal after install.
    # ---------------------------------------------------------------
    entry_points={
        "console_scripts": [
            "ghostpass=ghostpass.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
)