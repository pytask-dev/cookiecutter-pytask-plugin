"""Execute tasks."""
import shutil

from _pytask.config import hookimpl
from _pytask.mark_utils import get_specific_markers_from_task


@hookimpl
def pytask_execute_task_setup(task):
    """Check whether environment allows executing {{ cookiecutter.if_yes_tool_pretty_name }} files."""
    if get_specific_markers_from_task(task, "{{ cookiecutter.if_yes_marker_name }}"):
        if shutil.which("{{ cookiecutter.if_yes_command_line_tool }}") is None:
            raise RuntimeError(
                "{{ cookiecutter.if_yes_command_line_tool }} is needed to run {{ cookiecutter.if_yes_tool_pretty_name }} scripts, but it is not found on your PATH."
            )
