"""Contains test which ensure that the plugin works with pytask-parallel."""
import os
import textwrap
import time

import pytest
from conftest import needs_{{ cookiecutter.if_yes_command_line_tool }}
from pytask import cli

try:
    import pytask_parallel  # noqa: F401
except ImportError:
    _IS_PYTASK_PARALLEL_INSTALLED = False
else:
    _IS_PYTASK_PARALLEL_INSTALLED = True


pytestmark = pytest.mark.skipif(
    not _IS_PYTASK_PARALLEL_INSTALLED, reason="Tests require pytask-parallel."
)


@needs_{{ cookiecutter.if_yes_command_line_tool }}
@pytest.mark.end_to_end
def test_parallel_parametrization_over_source_files(runner, tmp_path):
    """Test parallelization over source files.

    Same as in README.rst.

    """
    os.chdir(tmp_path)

    source = """
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.parametrize(
        "depends_on, produces", [("script_1{{ cookiecutter.if_yes_executable_file_ending }}", "1.csv"), ("script_2{{ cookiecutter.if_yes_executable_file_ending }}", "2.csv")]
    )
    def task_execute_{{ cookiecutter.if_yes_command_line_tool }}():
        pass
    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(source))

    {{ cookiecutter.if_yes_marker_name }}_script = """FIXME FOR YOUR LANGUAGE
    Sys.sleep(2)
    saveRDS(1, file=paste0(1, ".csv"))
    """
    tmp_path.joinpath("script_1.r").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    Sys.sleep(2)
    saveRDS(2, file=paste0(2, ".csv"))
    """
    tmp_path.joinpath("script_2{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    start = time.time()
    result = runner.invoke(cli, [tmp_path.as_posix()])
    assert result.exit_code == 0
    duration_normal = time.time() - start

    for name in ["1.csv", "2.csv"]:
        tmp_path.joinpath(name).unlink()

    start = time.time()
    result = runner.invoke(cli, [tmp_path.as_posix(), "-n", 2])
    assert result.exit_code == 0
    duration_parallel = time.time() - start

    assert duration_parallel < duration_normal


@needs_{{ cookiecutter.if_yes_command_line_tool }}
@pytest.mark.end_to_end
def test_parallel_parametrization_over_source_file(runner, tmp_path):
    """Test parallelization over the same source file.

    Same as in README.rst.

    """
    os.chdir(tmp_path)

    source = """
    import pytask
    from pathlib import Path

    SRC = Path(__file__).parent

    @pytask.mark.depends_on("script{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.parametrize("produces, {{ cookiecutter.if_yes_marker_name }}", [
        (SRC / "0.csv", (1, SRC / "0.csv")), (SRC / "1.csv", (1, SRC / "1.csv"))
    ])
    def task_execute_{{ cookiecutter.if_yes_marker_name }}_script():
        pass
    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(source))

    {{ cookiecutter.if_yes_marker_name }}_script = """FIXME FOR YOUR LANGUAGE
    Sys.sleep(2)
    args <- commandArgs(trailingOnly=TRUE)
    number <- args[1]
    produces <- args[2]
    saveRDS(number, file=produces)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    start = time.time()
    result = runner.invoke(cli, [tmp_path.as_posix()])
    assert result.exit_code == 0
    duration_normal = time.time() - start

    for name in ["0.csv", "1.csv"]:
        tmp_path.joinpath(name).unlink()

    start = time.time()
    result = runner.invoke(cli, [tmp_path.as_posix(), "-n", 2])
    assert result.exit_code == 0
    duration_parallel = time.time() - start

    assert duration_parallel < duration_normal
