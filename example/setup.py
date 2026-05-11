from setuptools import setup, find_packages

# pip >=20
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

pages_requirements = list(
    parse_requirements("./docs/requirements.txt", session=PipSession())
)

# print(type(pages_requirements), pages_requirements)

setup(
    name="demo-sphinx",
    version="0.1.0",
    install_requires=[],
    extras_require={"dev": ["black"] + [x.requirement for x in pages_requirements]},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
