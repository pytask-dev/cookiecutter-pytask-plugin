import shutil

import pytest
from click.testing import CliRunner

{% if cookiecutter.keep_code_for_wrapping_subprocess_run == 'yes' %}
needs_{{ cookiecutter.if_yes_command_line_tool }} = pytest.mark.skipif(
    shutil.which("{{ cookiecutter.if_yes_command_line_tool }}") is None, reason="{{ cookiecutter.if_yes_command_line_tool }} needs to be installed."
){% endif %}

@pytest.fixture()
def runner():
    return CliRunner()
