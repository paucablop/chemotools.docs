import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Your Project Name'
copyright = '2025, Your Name'
author = 'Your Name'

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
html_theme_options = {
    "github_url": "https://github.com/paucablop/chemotools.docs",
    "announcement": "This is a demo site!",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/paucablop/chemotools.docs",
            "icon": "fab fa-github-square",
        },
    ],
    "use_edit_page_button": True,
    "show_toc_level": 2,
}

html_static_path = ['_static']