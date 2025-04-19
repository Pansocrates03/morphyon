from setuptools import setup, find_packages

setup(
    name="morphyon",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "watchdog",
        "fastapi",
        "uvicorn"
    ]
)