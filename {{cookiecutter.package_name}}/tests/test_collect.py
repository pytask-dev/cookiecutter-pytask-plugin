from contextlib import ExitStack as does_not_raise  # noqa: N813
from pathlib import Path

import pytest
from _pytask.mark import Mark
from _pytask.nodes import FilePathNode
from {{ cookiecutter.__package_name }}.collect import _get_node_from_dictionary
from {{ cookiecutter.__package_name }}.collect import _merge_all_markers
from {{ cookiecutter.__package_name }}.collect import _prepare_cmd_options
from {{ cookiecutter.__package_name }}.collect import pytask_collect_task
from {{ cookiecutter.__package_name }}.collect import pytask_collect_task_teardown
from {{ cookiecutter.__package_name }}.collect import {{ cookiecutter.if_yes_marker_name }}


class DummyClass:
    pass


def task_dummy():
    pass


@pytest.mark.unit
@pytest.mark.parametrize(
    "{{ cookiecutter.if_yes_marker_name }}_args, expected",
    [
        (None, []),
        ("--some-option", ["--some-option"]),
        (["--a", "--b"], ["--a", "--b"]),
    ],
)
def test_{{ cookiecutter.if_yes_marker_name }}({{ cookiecutter.if_yes_marker_name }}_args, expected):
    options = {{ cookiecutter.if_yes_marker_name }}({{ cookiecutter.if_yes_marker_name }}_args)
    assert options == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "marks, expected",
    [
        (
            [Mark("{{ cookiecutter.if_yes_marker_name }}", ("--a",), {}), Mark("{{ cookiecutter.if_yes_marker_name }}", ("--b",), {})],
            Mark("{{ cookiecutter.if_yes_marker_name }}", ("--a", "--b"), {}),
        ),
        (
            [Mark("{{ cookiecutter.if_yes_marker_name }}", ("--a",), {}), Mark("r", (), {"r": "--b"})],
            Mark("{{ cookiecutter.if_yes_marker_name }}", ("--a",), {"{{ cookiecutter.if_yes_marker_name }}": "--b"}),
        ),
    ],
)
def test_merge_all_markers(marks, expected):
    task = DummyClass()
    task.markers = marks
    out = _merge_all_markers(task)
    assert out == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "name, expected",
    [("task_dummy", True), ("invalid_name", None)],
)
def test_pytask_collect_task(name, expected):
    session = DummyClass()
    path = Path("some_path")
    task_dummy.pytaskmark = [Mark("{{ cookiecutter.if_yes_marker_name }}", (), {})]

    task = pytask_collect_task(session, path, name, task_dummy)

    if expected:
        assert task
    else:
        assert not task


@pytest.mark.unit
@pytest.mark.parametrize(
    "depends_on, produces, expectation",
    [
        (["script{{ cookiecutter.if_yes_executable_file_ending }}"], ["any_out.rds"], does_not_raise()),
        (["script.txt"], ["any_out.rds"], pytest.raises(ValueError)),
        (["input.csv", "script{{ cookiecutter.if_yes_executable_file_ending }}"], ["any_out.csv"], pytest.raises(ValueError)),
    ],
)
@pytest.mark.parametrize("{{ cookiecutter.if_yes_marker_name }}_source_key", ["source", "script"])
def test_pytask_collect_task_teardown(
    tmp_path, depends_on, produces, expectation, {{ cookiecutter.if_yes_marker_name }}_source_key
):
    session = DummyClass()
    session.config = {"{{ cookiecutter.if_yes_marker_name }}_source_key": {{ cookiecutter.if_yes_marker_name }}_source_key}

    task = DummyClass()
    task.path = tmp_path / "task_dummy.py"
    task.name = tmp_path.as_posix() + "task_dummy.py::task_dummy"
    task.depends_on = {
        i: FilePathNode.from_path(tmp_path / n) for i, n in enumerate(depends_on)
    }
    task.produces = {
        i: FilePathNode.from_path(tmp_path / n) for i, n in enumerate(produces)
    }
    task.markers = [Mark("{{ cookiecutter.if_yes_marker_name }}", (), {})]
    task.function = task_dummy
    task.function.pytaskmark = task.markers

    with expectation:
        pytask_collect_task_teardown(session, task)


@pytest.mark.unit
@pytest.mark.parametrize(
    "obj, key, expected",
    [
        (1, "asds", 1),
        (1, None, 1),
        ({"a": 1}, "a", 1),
        ({0: 1}, "a", 1),
    ],
)
def test_get_node_from_dictionary(obj, key, expected):
    result = _get_node_from_dictionary(obj, key)
    assert result == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "args",
    [
        [],
        ["a"],
        ["a", "b"],
    ],
)
@pytest.mark.parametrize("{{ cookiecutter.if_yes_marker_name }}_source_key", ["source", "script"])
def test_prepare_cmd_options(args, {{ cookiecutter.if_yes_marker_name }}_source_key):
    session = DummyClass()
    session.config = {"{{ cookiecutter.if_yes_marker_name }}_source_key": {{ cookiecutter.if_yes_marker_name }}_source_key}

    node = DummyClass()
    node.path = Path("script{{ cookiecutter.if_yes_executable_file_ending }}")
    task = DummyClass()
    task.depends_on = {"{{ cookiecutter.if_yes_marker_name }}_source_key": node}
    task.name = "task"

    result = _prepare_cmd_options(session, task, args)

    assert result == ["{{ cookiecutter.if_yes_command_line_tool }}", "script{{ cookiecutter.if_yes_executable_file_ending }}", *args]
