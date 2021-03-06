"""Parametrize tasks."""
from _pytask.config import hookimpl
from _pytask.mark import MARK_GEN as mark  # noqa: N811


@hookimpl
def pytask_parametrize_kwarg_to_marker(obj, kwargs):
    """Attach parametrized {{ cookiecutter.if_yes_command_line_tool }} arguments to the function with a marker."""
    if callable(obj):
        if "{{ cookiecutter.if_yes_marker_name }}" in kwargs:
            mark.{{ cookiecutter.if_yes_marker_name }}(kwargs.pop("{{ cookiecutter.if_yes_marker_name }}"))(obj)
