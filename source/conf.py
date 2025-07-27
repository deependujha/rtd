# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'My Documentation'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# -- MyST configuration -----------------------------------------------------
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "colon_fence",
    "linkify",
]

# -- Intersphinx configuration ----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- HTML options -----------------------------------------------------------
html_title = f"{project} {release}"
html_short_title = project
html_show_sourcelink = False
html_show_sphinx = False

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
