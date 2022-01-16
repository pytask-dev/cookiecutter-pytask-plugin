"""Configure pytask."""
from _pytask.config import hookimpl


@hookimpl
def pytask_parse_config(config, config_from_file):
    """Register the r marker."""
    config["markers"]["{{ cookiecutter.if_yes_marker_name }}"] = "Tasks which are executed with {{ cookiecutter.if_yes_tool_pretty_name }}."
    config["{{ cookiecutter.if_yes_marker_name }}_source_key"] = config_from_file.get("{{ cookiecutter.if_yes_marker_name }}_source_key", "source")
