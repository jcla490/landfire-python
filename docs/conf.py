"""Sphinx configuration."""
project = "Landfire"
author = "FireSci"
copyright = "2023, FireSci"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
