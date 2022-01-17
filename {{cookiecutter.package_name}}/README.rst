{{ cookiecutter.package_name }}
{% for _ in cookiecutter.package_name %}={% endfor %}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.package_name }}.svg
    :target: https://anaconda.org/conda-forge/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/conda/pn/conda-forge/{{ cookiecutter.package_name }}.svg
    :target: https://anaconda.org/conda-forge/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}
    :alt: PyPI - License
    :target: https://pypi.org/project/{{ cookiecutter.package_name }}

{% if cookiecutter.add_github_actions == "yes" %}.. image:: https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/main/main
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions?query=branch%3Amain
{% endif %}
{% if cookiecutter.add_readthedocs == "yes" %}.. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name | replace("_", "-") }}/badge/?version=latest
    :target: https://{{ cookiecutter.package_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
{% endif %}
{% if cookiecutter.add_codecov == "yes" %}.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}
{% endif %}
.. image:: https://results.pre-commit.ci/badge/github/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/main.svg
    :target: https://results.pre-commit.ci/latest/github/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/main
    :alt: pre-commit.ci status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


Installation
------------

{{ cookiecutter.package_name }} is available on `PyPI <https://pypi.org/project/{{
cookiecutter.package_name }}>`_ and `Anaconda.org <https://anaconda.org/conda-forge/{{
cookiecutter.package_name }}>`_. Install it with

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

    # or

    $ conda install -c conda-forge {{ cookiecutter.package_name }}

{% if cookiecutter.keep_code_for_wrapping_subprocess_run == 'yes' %}
You also need to have {{ cookiecutter.if_yes_tool_pretty_name }} installed and ``{{
cookiecutter.if_yes_command_line_tool }}`` on your command line. Test it by typing the
following on the command line

.. code-block:: console

    $ {{ cookiecutter.if_yes_command_line_tool }} --help

If an error is shown instead of a help page, you can install {{ cookiecutter.if_yes_command_line_tool }} ....


Usage
-----

Similarly to normal task functions which execute Python code, you define tasks to
execute scripts written in {{ cookiecutter.if_yes_command_line_tool }} with Python functions. The difference is that the
function body does not contain any logic, but the decorator tells pytask how to handle
the task.

Here is an example where you want to run ``script.{{ cookiecutter.if_yes_executable_file_ending }}``.

.. code-block:: python

    import pytask


    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on("script.{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.produces("out.csv")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

Note that, you need to apply the ``@pytask.mark.{{ cookiecutter.if_yes_marker_name }}`` marker so that {{ cookiecutter.package_name }} handles the
task.

If you are wondering why the function body is empty, know that {{ cookiecutter.package_name }} replaces the
body with a predefined internal function. See the section on implementation details for
more information.


Multiple dependencies and products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What happens if a task has more dependencies? Using a list, the {{ cookiecutter.if_yes_command_line_tool }} script which should be
executed must be found in the first position of the list.

.. code-block:: python

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on(["script.{{ cookiecutter.if_yes_executable_file_ending }}", "input.csv"])
    @pytask.mark.produces("out.csv")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

If you use a dictionary to pass dependencies to the task, {{ cookiecutter.package_name }} will, first, look
for a ``"source"`` key in the dictionary and, secondly, under the key ``0``.

.. code-block:: python

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on({"source": "script.{{ cookiecutter.if_yes_executable_file_ending }}", "input": "input.csv"})
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass


    # or


    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on({0: "script.{{ cookiecutter.if_yes_executable_file_ending }}", "input": "input.csv"})
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass


    # or two decorators for the function, if you do not assign a name to the input.


    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on({"source": "script.{{ cookiecutter.if_yes_executable_file_ending }}"})
    @pytask.mark.depends_on("input.csv")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass


Command Line Arguments
~~~~~~~~~~~~~~~~~~~~~~

The decorator can be used to pass command line arguments to ``{{ cookiecutter.if_yes_command_line_tool }}``. See the
following example.

.. code-block:: python

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}("value")
    @pytask.mark.depends_on("script.{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.produces("out.csv")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

And in your ``script.{{ cookiecutter.if_yes_executable_file_ending }}``, you can intercept the value with

.. code-block:: {{ cookiecutter.if_yes_command_line_tool }}

    FIXME FOR YOUR LANGUAGE
    args <- commandArgs(trailingOnly=TRUE)
    arg <- args[1]  # holds ``"value"``


Parametrization
~~~~~~~~~~~~~~~

You can also parametrize the execution of scripts, meaning executing multiple {{ cookiecutter.if_yes_command_line_tool }} scripts
as well as passing different command line arguments to the same {{ cookiecutter.if_yes_command_line_tool }} script.

The following task executes two {{ cookiecutter.if_yes_command_line_tool }} scripts which produce different outputs.

.. code-block:: python

    from src.config import BLD, SRC


    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.parametrize(
        "depends_on, produces",
        [(SRC / "script_1{{ cookiecutter.if_yes_executable_file_ending }}", BLD / "1.csv"), (SRC / "script_2{{ cookiecutter.if_yes_executable_file_ending }}", BLD / "2.csv")],
    )
    def task_execute_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

And the R script includes something like

.. code-block:: r

    args <- commandArgs(trailingOnly=TRUE)
    produces <- args[1]  # holds the path

If you want to pass different command line arguments to the same {{ cookiecutter.if_yes_command_line_tool }} script, you have to
include the ``@pytask.mark.{{ cookiecutter.if_yes_marker_name }}`` decorator in the parametrization just like with
``@pytask.mark.depends_on`` and ``@pytask.mark.produces``.

.. code-block:: python

    @pytask.mark.depends_on("script.{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.parametrize(
        "produces, {{ cookiecutter.if_yes_marker_name }}",
        [(BLD / "output_1.csv", "1"), (BLD / "output_2.csv", "2")],
    )
    def task_execute_{{ cookiecutter.if_yes_marker_name }}_script():
        pass


Configuration
-------------

If you want to change the name of the key which identifies the {{ cookiecutter.if_yes_command_line_tool }} script, change the
following default configuration in your pytask configuration file.

.. code-block:: ini

    {{ cookiecutter.if_yes_marker_name }}_source_key = source


Implementation Details
----------------------

The plugin is a convenient wrapper around

.. code-block:: python

    import subprocess

    subprocess.run(["{{ cookiecutter.if_yes_command_line_tool }}", "script.{{ cookiecutter.if_yes_executable_file_ending }}"], check=True)

to which you can always resort to when the plugin does not deliver functionality you
need.

It is not possible to enter a post-mortem debugger when an error happens in the {{ cookiecutter.if_yes_command_line_tool }} script
or enter the debugger when starting the script. If there exists a solution for that,
hints as well as contributions are highly appreciated.
{% endif %}

Changes
-------

Consult the `release notes <CHANGES.rst>`_ to find out about what is new.
