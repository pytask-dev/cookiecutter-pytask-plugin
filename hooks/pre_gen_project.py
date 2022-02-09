"""This module contains hooks which are executed before the template is rendered."""
from __future__ import annotations

import re

MODULE_REGEX = r"^[-_a-zA-Z0-9]*$"
ENVIRON_REGEX = r"^[-_a-zA-Z0-9]*$"
PYTHONVERSION_REGEX = r"^(3)\.(7|8|9|10)$"

EXCEPTION_MSG_MODULE_NAME = """
ERROR: The project slug ({}) is not a valid Python module name.
Please do not use anything other than letters, numbers, underscores '_',
and minus signs '-'.
"""

EXCEPTION_MSG_ENVIRON_NAME = """
ERROR: The project slug ({}) is not a valid conda environment name.
Please do not use anything other than letters, numbers, underscores '_',
and minus signs '-'.
"""


_ = """{{ cookiecutter.update(
    {
        "__package_name":
        cookiecutter.package_name|lower|replace(' ', '_')|replace('-', '_'),
    }
)}}"""


def main():
    """Apply pre-generation hooks."""
    module_name = "{{ cookiecutter.__package_name }}"

    if not re.match(MODULE_REGEX, module_name):
        raise ValueError(EXCEPTION_MSG_MODULE_NAME.format(module_name))

    environment_name = "{{ cookiecutter.conda_environment_name }}"

    if not re.match(ENVIRON_REGEX, environment_name):
        raise ValueError(EXCEPTION_MSG_ENVIRON_NAME.format(environment_name))

    python_version = "{{ cookiecutter.python_version }}"

    if not re.match(PYTHONVERSION_REGEX, python_version):
        raise ValueError("ERROR: The python version must be >= 3.7")  # noqa: TC003


if __name__ == "__main__":
    main()
