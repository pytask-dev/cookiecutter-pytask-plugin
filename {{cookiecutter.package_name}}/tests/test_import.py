from __future__ import annotations

import {{ cookiecutter.__package_name }}


def test_import():
    assert hasattr({{ cookiecutter.__package_name }}, "__version__")
