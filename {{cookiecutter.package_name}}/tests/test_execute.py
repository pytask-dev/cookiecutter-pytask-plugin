import os
import textwrap
from contextlib import ExitStack as does_not_raise  # noqa: N813

import pytest
from _pytask.mark import Mark
from conftest import needs_{{ cookiecutter.if_yes_command_line_tool }}
from pytask import main
from {{ cookiecutter.__package_name }}.execute import pytask_execute_task_setup


class DummyTask:
    pass


@pytest.mark.unit
@pytest.mark.parametrize(
    "found_{{ cookiecutter.if_yes_command_line_tool }}, expectation",
    [
        (True, does_not_raise()),
        (None, pytest.raises(RuntimeError)),
    ],
)
def test_pytask_execute_task_setup(monkeypatch, found_{{ cookiecutter.if_yes_command_line_tool }}, expectation):
    """Make sure that the task setup raises errors."""
    # Act like r is installed since we do not test this.
    monkeypatch.setattr("{{ cookiecutter.__package_name }}.execute.shutil.which", lambda x: found_{{ cookiecutter.if_yes_command_line_tool }})

    task = DummyTask()
    task.markers = [Mark("{{ cookiecutter.if_yes_marker_name }}", (), {})]

    with expectation:
        pytask_execute_task_setup(task)


@needs_{{ cookiecutter.if_yes_command_line_tool }}
@pytest.mark.end_to_end
@pytest.mark.parametrize(
    "depends_on",
    ["'script{{ cookiecutter.if_yes_executable_file_ending }}'", {"source": "script{{ cookiecutter.if_yes_executable_file_ending }}"}, {0: "script{{ cookiecutter.if_yes_executable_file_ending }}"}, {"script": "script{{ cookiecutter.if_yes_executable_file_ending }}"}],
)
def test_run_{{ cookiecutter.if_yes_marker_name }}_script(tmp_path, depends_on):
    task_source = f"""
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on({depends_on})
    @pytask.mark.produces("out.txt")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    file_descriptor <- file("out.txt")
    writeLines(c("So, so you think you can tell heaven from hell?"), file_descriptor)
    close(file_descriptor)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    if (
        isinstance(depends_on, dict)
        and "source" not in depends_on
        and 0 not in depends_on
    ):
        tmp_path.joinpath("pytask.ini").write_text("[pytask]\nr_source_key = script")

    os.chdir(tmp_path)
    session = main({"paths": tmp_path})

    assert session.exit_code == 0
    assert tmp_path.joinpath("out.txt").exists()


@pytest.mark.end_to_end
def test_raise_error_if_{{ cookiecutter.if_yes_command_line_tool }}_is_not_found(tmp_path, monkeypatch):
    task_source = """
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.depends_on("script{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.produces("out.txt")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    file_descr <- file("out.txt")
    writeLines(c("Birds flying high you know how I feel."), file_descr)
    close(file_descr)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    # Hide {{ cookiecutter.if_yes_command_line_tool }} if available.
    monkeypatch.setattr("{{ cookiecutter.__package_name }}.execute.shutil.which", lambda x: None)

    session = main({"paths": tmp_path})

    assert session.exit_code == 1
    assert isinstance(session.execution_reports[0].exc_info[1], RuntimeError)


@needs_{{ cookiecutter.if_yes_command_line_tool }}
@pytest.mark.end_to_end
def test_run_{{ cookiecutter.if_yes_marker_name }}_script_w_saving_workspace(tmp_path):
    """Save workspace while executing the script."""
    task_source = """
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}("--save")
    @pytask.mark.depends_on("script{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.produces("out.txt")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    file_descr <- file("out.txt")
    writeLines(c("Birds flying high you know how I feel."), file_descr)
    close(file_descr)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    os.chdir(tmp_path)
    session = main({"paths": tmp_path})

    assert session.exit_code == 0
    assert tmp_path.joinpath("out.txt").exists()


@needs_{{ cookiecutter.if_yes_command_line_tool }}
@pytest.mark.end_to_end
def test_run_{{ cookiecutter.if_yes_marker_name }}_script_w_wrong_cmd_option(tmp_path):
    """Apparently, RScript simply discards wrong cmd options -- hopefully {{ cookiecutter.if_yes_command_line_tool }} does better."""
    task_source = """
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}("--wrong-flag")
    @pytask.mark.depends_on("script{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.produces("out.txt")
    def task_run_{{ cookiecutter.if_yes_marker_name }}_script():
        pass

    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    file_descr <- file("out.txt")
    writeLines(c("Birds flying high you know how I feel."), file_descr)
    close(file_descr)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    os.chdir(tmp_path)
    session = main({"paths": tmp_path})

    assert session.exit_code == 0
