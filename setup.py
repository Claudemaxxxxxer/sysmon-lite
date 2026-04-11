from setuptools import setup, find_packages

setup(
    name="sysmon-lite",
    version="0.3.0",
    description="Tiny system monitor",
    author="n0ctis",
    packages=find_packages(),
    entry_points={"console_scripts": ["sysmon=sysmon.cli:main"]},
    python_requires=">=3.8",
)
