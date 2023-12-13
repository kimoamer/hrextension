from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hrextension/__init__.py
from hrextension import __version__ as version

setup(
	name="hrextension",
	version=version,
	description="An Extension for hrms",
	author="Hak3em",
	author_email="abdoamer19@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
