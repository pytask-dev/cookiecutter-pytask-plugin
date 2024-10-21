"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

# -- Project information -----------------------------------------------------
from __future__ import annotations

project = "cookiecutter-pytask"
author = "Tobias Raabe"
copyright = f"2021, {author}"  # noqa: A001

# The version, including alpha/beta/rc tags, but not commit hash and datestamps
release = "1.0.0"
# The short X.Y version.
version = "1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions coming
# with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxext.opengraph",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_panels",
    "autoapi.extension",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories to
# ignore when looking for source files. This pattern also affects html_static_path and
# html_extra_path.
exclude_patterns = ["build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# Configuration for autoapi to generate and API page.
autoapi_type = "python"
autoapi_dirs = ["../../hooks"]
autoapi_keep_files = False
autoapi_add_toctree_entry = False

# Remove prefixed $ for bash, >>> for Python prompts, and In [1]: for IPython prompts.
copybutton_prompt_text = r"\$ |>>> |In \[\d\]: "
copybutton_prompt_is_regexp = True

# Use these roles to create links to github users and pull requests.
_repo = "https://github.com/pytask-dev/cookiecutter-pytask-project"
extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
    "issue": (f"{_repo}/issues/%s", "issue #"),
    "pull": (f"{_repo}/pull/%s", "pull request #"),
    "user": ("https://github.com/%s", "@"),
}

# Link objects to other documentations.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "pytask": ("https://pytask-dev.readthedocs.io/en/stable/", None),
}

# MyST
myst_enable_extensions = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of
# builtin themes.
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here, relative
# to this directory. They are copied after the builtin static files, so a file named
# "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
