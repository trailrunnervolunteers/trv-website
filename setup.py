from setuptools import find_packages, setup

setup(
    name="trv",
    version="1.0",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
)
