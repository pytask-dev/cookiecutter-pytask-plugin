# {{ cookiecutter.package_name }}

{% if cookiecutter.add_github_actions == "yes"
%}[![image](https://img.shields.io/github/actions/workflow/status/{{
cookiecutter.github_username }}/{{ cookiecutter.package_name
}}/main.yml?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{
cookiecutter.package_name }}/actions?query=branch%3Amain) {% endif %} {% if
cookiecutter.add_readthedocs == "yes" %}[![image](https://readthedocs.org/projects/{{
cookiecutter.package_name | replace("_", "-") }}/badge/?version=stable)](https://{{
cookiecutter.package_name | replace("_", "-") }}.readthedocs.io/en/stable/?badge=stable)
{% endif %} {% if cookiecutter.add_codecov == "yes"
%}[![image](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{
cookiecutter.package_name }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{
cookiecutter.github_username }}/{{ cookiecutter.package_name }}) {% endif %}
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/{{
cookiecutter.github_username }}/{{ cookiecutter.package_name
}}/main.svg)](https://results.pre-commit.ci/latest/github/{{
cookiecutter.github_username }}/{{ cookiecutter.package_name }}/main)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Installation

{{ cookiecutter.package_name }} is available on [PyPI](https://pypi.org/project/{{
cookiecutter.package_name }}) and [Anaconda.org](https://anaconda.org/conda-forge/{{
cookiecutter.package_name }}). Install it with

```console
$ pip install {{ cookiecutter.package_name }}

# or

$ conda install -c conda-forge {{ cookiecutter.package_name }}
```

## Changes

Consult the [release notes](CHANGES.md) to find out about what is new.
