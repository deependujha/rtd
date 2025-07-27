# Documentation Site

This is a Sphinx-based documentation site configured for GitHub Pages hosting.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build the documentation:
```bash
make html
```

3. Serve locally for development:
```bash
make serve
```

## GitHub Pages Setup

1. Push this repository to GitHub
2. Go to Settings > Pages in your GitHub repository
3. Set Source to "GitHub Actions"
4. The documentation will be automatically built and deployed on push to main

## Structure

- `source/` - Documentation source files
- `build/` - Generated HTML files (not committed)
- `docs/` - GitHub Pages output directory
- `.github/workflows/` - GitHub Actions for automated deployment
