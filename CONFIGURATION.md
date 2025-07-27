# Documentation Site Configuration Examples

This file contains example configurations for different types of documentation sites.

## Basic Project Documentation

For a standard software project, update `source/conf.py`:

```python
project = 'Your Project Name'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.0.0'
```

## API Documentation

If you have Python code to document, place your modules in a `src/` directory and update the conf.py:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    # ... other extensions
]
```

## Theme Customization

### Read the Docs Theme Options

```python
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  # Your Google Analytics ID
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
```

### Custom Logo

Place your logo in `source/_static/logo.png` and add:

```python
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'
```

## GitHub Repository Integration

Add repository links to your documentation:

```python
html_context = {
    "display_github": True,
    "github_user": "your-username",
    "github_repo": "your-repo-name",
    "github_version": "main",
    "conf_py_path": "/source/",
}
```

## Additional Extensions

### Markdown Support
Already included with MyST parser. You can write pages in `.md` format.

### Copy Button for Code Blocks
Already included with `sphinx-copybutton`.

### API Documentation from Docstrings
Use `sphinx.ext.autodoc` and `sphinx.ext.napoleon` for Google/NumPy style docstrings.

### Jupyter Notebook Integration
Add to requirements.txt and conf.py:

```bash
# requirements.txt
nbsphinx==0.9.1
```

```python
# conf.py
extensions = [
    # ... existing extensions
    'nbsphinx',
]
```

## Multi-language Documentation

For international documentation:

```python
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
```

## PDF Generation

To generate PDF documentation:

```bash
# Add to requirements.txt
rst2pdf==0.99

# Build PDF
make latexpdf
```

## Search Integration

Sphinx includes built-in search. For external search:

```python
# Add Algolia DocSearch
html_theme_options = {
    'search_bar_text': 'Search the docs...',
}
```
