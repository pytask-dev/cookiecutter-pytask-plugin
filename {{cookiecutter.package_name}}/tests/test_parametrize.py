import os
import textwrap

import pytest
from conftest import needs_rscript
from pytask import main


@needs_rscript
@pytest.mark.end_to_end
def test_parametrized_execution_of_r_script(tmp_path):
    task_source = """
    import pytask

    @pytask.mark.{{ cookiecutter.if_yes_marker_name }}
    @pytask.mark.parametrize("depends_on, produces", [
        ("script_1{{ cookiecutter.if_yes_executable_file_ending }}", "0.txt"),
        ("script_2{{ cookiecutter.if_yes_executable_file_ending }}", "1.txt"),
    ])
    def task_run_r_script():
        pass
    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    for name, content, out in [
        ("script_1{{ cookiecutter.if_yes_executable_file_ending }}", "Cities breaking down on a camel's back", "0.txt"),
        ("script_2{{ cookiecutter.if_yes_executable_file_ending }}", "They just have to go 'cause they don't know whack", "1.txt"),
    ]:
        {{ cookiecutter.if_yes_marker_name }}_script = f"""
        file_descr <- file("{out}")
        writeLines(c("{content}"), file_descr)
        close(file_descr)
        """
        tmp_path.joinpath(name).write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    os.chdir(tmp_path)
    session = main({"paths": tmp_path})

    assert session.exit_code == 0
    assert tmp_path.joinpath("0.txt").exists()
    assert tmp_path.joinpath("1.txt").exists()


@needs_rscript
@pytest.mark.end_to_end
def test_parametrize_r_options_and_product_paths(tmp_path):
    task_source = """
    import pytask
    from pathlib import Path

    SRC = Path(__file__).parent

    @pytask.mark.depends_on("script{{ cookiecutter.if_yes_executable_file_ending }}")
    @pytask.mark.parametrize("produces, {{ cookiecutter.if_yes_marker_name }}", [
        (SRC / "0.rds", (0, SRC / "0.rds")), (SRC / "1.rds", (1, SRC / "1.rds"))
    ])
    def task_execute_r_script():
        pass
    """
    tmp_path.joinpath("task_dummy.py").write_text(textwrap.dedent(task_source))

    {{ cookiecutter.if_yes_marker_name }}_script = """
    args <- commandArgs(trailingOnly=TRUE)
    number <- args[1]
    produces <- args[2]
    saveRDS(number, file=produces)
    """
    tmp_path.joinpath("script{{ cookiecutter.if_yes_executable_file_ending }}").write_text(textwrap.dedent({{ cookiecutter.if_yes_marker_name }}_script))

    os.chdir(tmp_path)
    session = main({"paths": tmp_path})

    assert session.exit_code == 0
    assert tmp_path.joinpath("0.rds").exists()
    assert tmp_path.joinpath("1.rds").exists()
