import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Chemotools'
copyright = '2025, chemotools'
author = 'Pau Cabaneros'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# Language settings
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
gettext_uuid = True

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'pydata_sphinx_theme'

# GitHub context and other variables
html_context = {
    "github_user": "paucablop",
    "github_repo": "chemotools.docs",
    "github_version": "main",
    "doc_path": "docs/source",
    # Language settings
    "languages": [
        ('en', 'English'),
        ('es', 'Español'),
        ('zh', '中文'),
    ],
    "language": "en",
    "default_language": "en",
}

html_theme_options = {
    "github_url": "https://github.com/paucablop/chemotools.docs",
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_end": ["theme-switcher", "navbar-icon-links"]
}

# Make sure static files are properly configured
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

templates_path = ['_templates']