from setuptools import find_packages, setup

setup(
    name="lab2",
    packages=find_packages(exclude=["lab2_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
