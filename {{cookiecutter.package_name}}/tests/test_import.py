from __future__ import annotations

import {{ cookiecutter.package_name }}


def test_import():
    assert hasattr({{ cookiecutter.package_name }}, "__version__")
