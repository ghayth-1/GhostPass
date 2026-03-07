from setuptools import setup, find_packages

setup(
    name="ghostpass",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "ghostpass=ghostpass_core.cli:main",
        ],
    },
)
