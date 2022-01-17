cookiecutter-pytask-plugin
==========================

.. image:: https://img.shields.io/github/license/pytask-dev/cookiecutter-pytask-plugin
    :alt: MIT license
    :target: https://pypi.org/project/pytask

.. image:: https://readthedocs.org/projects/cookiecutter-pytask-plugin/badge/?version=latest
    :target: https://cookiecutter-pytask-plugin.readthedocs.io/en/latest

.. image:: https://img.shields.io/github/workflow/status/pytask-dev/cookiecutter-pytask-plugin/main/main
   :target: https://github.com/pytask-dev/cookiecutter-pytask-plugin/actions?query=branch%3Amain

.. image:: https://codecov.io/gh/pytask-dev/cookiecutter-pytask-plugin/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/pytask-dev/cookiecutter-pytask-plugin

.. image:: https://results.pre-commit.ci/badge/github/pytask-dev/cookiecutter-pytask-plugin/main.svg
    :target: https://results.pre-commit.ci/latest/github/pytask-dev/cookiecutter-pytask-plugin/main
    :alt: pre-commit.ci status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


This repository contains a minimal cookiecutter template for a project with `pytask
<https://github.com/pytask-dev/pytask>`_ .


Usage
-----

First, install cookiecutter.

.. code-block:: console

    $ pip install cookiecutter

    $ conda install -c conda-forge cookiecutter

Then, set up the template with

.. code-block:: console

    $ cookiecutter https://github.com/pytask-dev/cookiecutter-pytask-plugin


FAQ
---

Q: Why are the source files nested in ``src/<{{ cookiecutter.__package_name }}>``?

A: This is called the src layout and the advantages are discussed in this `article by
Hynek Schlawack <https://hynek.me/articles/testing-packaging/>`_.

Although the article discusses the src layout in terms of Python packages, it is also
beneficial to structure a project the same way.
