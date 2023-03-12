"""Sphinx configuration."""
project = "landfire-python"
author = "FireSci"
copyright = "2023, FireSci"
extensions = [
    "enum_tools.autoenum",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "myst_parser",
]
autodoc_typehints = "description"

# theme
html_theme = "furo"
html_title = project
# pygments_style = "sphinx"
# pygments_dark_style = "monokai"
