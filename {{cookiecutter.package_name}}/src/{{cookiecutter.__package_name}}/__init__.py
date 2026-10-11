"""This module contains the main namespace of the package."""

from importlib.metadata import version

__version__ = version("{{ cookiecutter.__package_name }}")

__all__ = ["__version__"]
