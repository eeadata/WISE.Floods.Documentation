# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "WISE Floods Documentation"
author = "WISE Team"
copyright = "2026, Tracasa"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]