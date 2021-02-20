from setuptools import setup

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.readlines()


setup(
    name="aiodav",
    version="",
    packages=["aiodav", "aiodav.views"],
    url="https://github.com/GerbenAaltink/aiodav",
    license="",
    author="Gerben Aaltink",
    author_email="aiodav",
    description="Webdav webserver views",
    install_requires=requirements,
)
