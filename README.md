# cookiecutter-pytask-plugin

[![MIT license](https://img.shields.io/github/license/pytask-dev/cookiecutter-pytask-plugin)](https://github.com/pytask-dev/cookiecutter-pytask-plugin)
[![image](https://readthedocs.org/projects/cookiecutter-pytask-plugin/badge/?version=latest)](https://cookiecutter-pytask-plugin.readthedocs.io/en/latest)
[![image](https://img.shields.io/github/actions/workflow/status/pytask-dev/cookiecutter-pytask-plugin/main.yml?branch=main)](https://github.com/pytask-dev/cookiecutter-pytask-plugin/actions?query=branch%3Amain)
[![image](https://codecov.io/gh/pytask-dev/cookiecutter-pytask-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/pytask-dev/cookiecutter-pytask-plugin)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pytask-dev/cookiecutter-pytask-plugin/main.svg)](https://results.pre-commit.ci/latest/github/pytask-dev/cookiecutter-pytask-plugin/main)
[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains a minimal cookiecutter template for a plugin for
[pytask](https://github.com/pytask-dev/pytask) .

## Usage

First, install cookiecutter.

```console
$ pip install cookiecutter

$ conda install -c conda-forge cookiecutter
```

Then, set up the template for the new plugin with

```console
$ cookiecutter https://github.com/pytask-dev/cookiecutter-pytask-plugin
```

## FAQ

Q: Why are the source files nested in `src/<{{ cookiecutter.__package_name }}>`?

A: This is called the src layout. This
[article by Hynek Schlawack](https://hynek.me/articles/testing-packaging/) discusses the
advantages of this layout in detail.
