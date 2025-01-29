import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Chemotools'
copyright = '2025, Chemotools'
author = 'Pau Cabaneros'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
]

# Add any paths that contain templates here
templates_path = ['_templates']
exclude_patterns = []

# HTML theme settings
html_theme = 'pydata_sphinx_theme'

# GitHub context
html_context = {
    "github_user": "paucablop",  # Replace with your GitHub username
    "github_repo": "chemotools.docs",      # Replace with your repository name
    "github_version": "main",
}

html_theme_options = {
    "github_url": "https://github.com/paucablop/chemotools.docs",
    "announcement": "This is a demo site!",
    "use_edit_page_button": True,
    "show_toc_level": 2,
}

# The theme to use for HTML and HTML Help pages.
html_static_path = ['_static']