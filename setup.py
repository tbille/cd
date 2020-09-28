from setuptools import setup


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="cdrom",
    version="disc-compact",
    install_requires=requirements,
    scripts=["cdrom.py"],
)
