from __future__ import annotations

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
