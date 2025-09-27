# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "chemotools"
copyright = "2025, chemotools"
author = "Pau Cabaneros"
# release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "nbsphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/_main_page/logo-light-3.svg"
html_favicon = (
    "_static/_main_page/favicon2.svg"  # or favicon.png if using PNG
)

# Optional theme customization
html_theme_options = {
    "show_prev_next": True,
    "logo": {
        "image_light": "_static/_main_page/logo-light-3.svg",
        "image_dark": "_static/_main_page/logo-dark-3.svg",
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
        },
    ],
    "use_edit_page_button": False,
    "navigation_with_keys": False,
}

# Only include public members unless explicitly told otherwise
autodoc_default_options = {
    "members": True,
    "undoc-members": False,     # don't include things without docstrings
    "private-members": False,   # skip _private methods
    "special-members": False,   # skip __special__ methods
}


# optional but nice:
autodoc_member_order = "bysource"
autoclass_content = "both"
autosummary_generate = True     # generate stub pages automatically
autosummary_imported_members = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]

# Tell autosummary where to find templates
autosummary_generate = True
templates_path = ['_templates']
autosummary_imported_members = True


# Napoleon settings (for NumPy-style docstrings)
napoleon_google_docstring = False
napoleon_numpy_docstring = True

napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False

napoleon_use_ivar = True  # <-- KEY: ensures Attributes become proper fields
napoleon_use_param = True
napoleon_use_rtype = True

# Intersphinx to resolve external refs from sklearn docstrings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
}

# Be tolerant to external labels missing in intersphinx
nitpicky = False

# Exclude autosummary per-method/attribute pages (keep class pages)
exclude_patterns = [
    "_methods/generated/*.*.*.*.rst",
]
