from __future__ import annotations

import shutil
import subprocess
import sys

import pytest


@pytest.mark.end_to_end
def test_bake_project(cookies):
    major, minor = sys.version_info[:2]
    python_version = f"{major}.{minor}"

    result = cookies.bake(
        extra_context={
            "package_name": "pytask-matlab",
            "python_version": python_version,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "pytask-matlab"
    assert result.project_path.is_dir()


@pytest.mark.end_to_end
def test_remove_readthedocs(cookies):
    result = cookies.bake(extra_context={"add_readthedocs": "no"})

    rtd_config = result.project_path.joinpath(".readthedocs.yaml")
    readme = result.project_path.joinpath("README.md").read_text()

    assert result.exit_code == 0
    assert result.exception is None

    assert not rtd_config.exists()
    assert "readthedocs" not in readme


@pytest.mark.end_to_end
def test_remove_github_actions(cookies):
    result = cookies.bake(extra_context={"add_github_actions": "no"})

    ga_config = result.project_path.joinpath(".github", "workflows", "main.yml")
    readme = result.project_path.joinpath("README.md").read_text()

    assert result.exit_code == 0
    assert result.exception is None

    assert not ga_config.exists()
    assert "github/workflow/status" not in readme


@pytest.mark.end_to_end
def test_remove_license(cookies):
    result = cookies.bake(extra_context={"open_source_license": "Not open source"})

    license_ = result.project_path.joinpath("LICENSE")

    assert result.exit_code == 0
    assert result.exception is None

    assert not license_.exists()


@pytest.mark.end_to_end
@pytest.mark.parametrize("license_name", ["MIT", "Not open source"])
def test_install_generated_plugin(cookies, tmp_path, license_name):
    uv = shutil.which("uv")
    assert uv is not None
    result = cookies.bake(
        extra_context={
            "package_name": "pytask-template-check",
            "open_source_license": license_name,
        }
    )
    assert result.exit_code == 0
    project_path = tmp_path / "project"
    shutil.copytree(
        result.project_path, project_path, ignore=shutil.ignore_patterns(".git")
    )
    wheel_dir = tmp_path / "dist"
    subprocess.run(  # noqa: S603
        (uv, "build", "--wheel", "--out-dir", str(wheel_dir)),
        cwd=project_path,
        check=True,
    )
    wheel = next(wheel_dir.glob("*.whl"))
    source = """
from importlib import metadata
from pytask import cli
from click.testing import CliRunner
import pytask_template_check

entry_point, = metadata.entry_points(
    group="pytask", name="pytask_template_check"
)
assert entry_point.load().__name__ == "pytask_template_check.plugin"
assert metadata.version("pytask-template-check") == "0.1.0"
assert pytask_template_check.__version__ == metadata.version("pytask-template-check")
assert CliRunner().invoke(cli, ["--help"]).exit_code == 0
"""
    subprocess.run(  # noqa: S603
        (
            uv,
            "run",
            "--no-project",
            "--isolated",
            "--python",
            sys.executable,
            "--with",
            str(wheel),
            "python",
            "-c",
            source,
        ),
        cwd=project_path,
        check=True,
    )
