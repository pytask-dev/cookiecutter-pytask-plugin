import pytest
from pytask import main


@pytest.mark.end_to_end
def test_marker_is_configured(tmp_path):
    session = main({"paths": tmp_path})

    assert "{{ cookiecutter.if_yes_marker_name }}" in session.config["markers"]
