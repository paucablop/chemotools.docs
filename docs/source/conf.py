# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'chemotools.docs'
copyright = '2025, Pau Cabaneros'
author = 'Pau Cabaneros'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "pydata_sphinx_theme"
]

html_theme = "pydata_sphinx_theme"

# Optional theme customization
html_theme_options = {
    "show_prev_next": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/paucablop/chemotools.docs",  # replace with your repo
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
    ],
    "use_edit_page_button": False,
    "navigation_with_keys": False,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
