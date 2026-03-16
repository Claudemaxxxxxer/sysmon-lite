from setuptools import setup, find_packages

setup(
    name="sysmon-lite",
    version="0.1.0",
    description="Tiny system monitor",
    author="n0ctis",
    author_email="HiddenTrigger@proton.me",
    packages=find_packages(),
    entry_points={"console_scripts": ["sysmon=sysmon.cli:main"]},
    python_requires=">=3.8",
)
