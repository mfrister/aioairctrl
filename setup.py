from setuptools import setup, find_packages

setup(
    name="phipsair",
    version="0.3.0",
    description="phipsair allwos controlling Philips air purifiers via encrypted CoAP.",
    author="betaboon",
    url="https://github.com/mfrister/phipsair",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "aiocoap>=0.4.1, <0.5",
        "pycryptodomex>=3.13, <4.0",
    ],
    entry_points={
        "console_scripts": [
            "phipsair=phipsair.__main__:main",
        ],
    },
)
