# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys, os

# Check if this is on ReadTheDocs, which sets a specific environment variable
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

if on_rtd:
   extensions = ['sphinx.ext.autodoc',
                 'myst_parser',
                 'sphinx_rtd_theme',
                 'sphinx.ext.todo', 
                 'sphinx.ext.imgmath', 
                 'sphinx.ext.mathjax',
                 'sphinxcontrib.mermaid',  
                 'sphinx.ext.graphviz']
else:
   extensions = ['sphinx.ext.autodoc',
                 'myst_parser',
                 'sphinx_rtd_theme',
                 'sphinx.ext.todo', 
                 'sphinx.ext.imgmath', 
                 'sphinx.ext.mathjax', 
                 'sphinx.ext.graphviz', 
                 'sphinxcontrib.bibtex', 
                 'sphinxcontrib.mermaid', 
                 'sphinxcontrib.xlsxtable']

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
bibtex_bibfiles = ['./_sharedFiles/bibliography.bib'] 

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','*.txt']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Support for todo items: If this is True, todo and todolist produce output, else they produce nothing. The default is False.

todo_include_todos = True
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'customTable.css'
]

html_theme_options = {
    "navigation_depth": -1,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}
project = 'Water Dataflows'
copyright = '11/05/2026, Docsource from https://eea1.sharepoint.com/teams/cws'
author = 'Ramya Bandi'
release = '1.0'