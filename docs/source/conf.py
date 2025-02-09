# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'chemotools'
copyright = '2025, chemotools'
author = 'Pau Cabaneros'
#release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "nbsphinx",
]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/_main_page/logo-light.svg"
html_favicon = "_static/_main_page/chemotools_logo_large.svg"  # or favicon.png if using PNG

# Optional theme customization
html_theme_options = {
    "show_prev_next": True,
    "logo": {
        "image_light": "_static/_main_page/logo-light.svg",
        "image_dark": "_static/_main_page/logo-dark.svg",
    },
    "navbar_align": "left",
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],  # Added theme-switcher here
    "show_nav_level": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/paucablop/chemotools",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/company/chemotools",
        "icon": "fab fa-linkedin",
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
html_css_files = [
    'custom.css',
]
