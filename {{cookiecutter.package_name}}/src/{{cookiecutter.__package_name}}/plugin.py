"""Register hook specifications and implementations."""
from _pytask.config import hookimpl
{% if cookiecutter.keep_code_for_wrapping_subprocess_run == 'yes' %}from {{ cookiecutter.__package_name }} import collect
from {{ cookiecutter.__package_name }} import config
from {{ cookiecutter.__package_name }} import execute
from {{ cookiecutter.__package_name }} import parametrize
{% endif %}

@hookimpl
def pytask_add_hooks(pm):
    """Register hook implementations."""
    {% if cookiecutter.keep_code_for_wrapping_subprocess_run == 'yes' %}pm.register(collect)
    pm.register(config)
    pm.register(execute)
    pm.register(parametrize)
{% endif %}