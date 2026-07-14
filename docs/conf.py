# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "WISE Floods Documentation"
author = "WISE Team"
copyright = "2026"

extensions = [
    "myst_parser",
    "sphinx_design",
]

source_suffix = {
    ".md": "markdown",
}
 
myst_enable_extensions = [
    "colon_fence",
]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_theme_options = {
    "logo": {
        "image_light": "_static/wise.svg",
        "image_dark": "_static/wise-freshwater.svg",
        "text": "Floods Directive",
    },
}


html_css_files = [
    "customTheme.css",
    "customTable.css",
]

html_js_files = [
    "js/mermaid-zoom.js",
]
