Contributing
============

We welcome contributions to this project! This guide will help you get started.

Development Setup
-----------------

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/your-repo.git
cd your-repo
```

### Development Environment

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:

```bash
pip install -e ".[dev]"
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

Code Standards
--------------

### Style Guide

We follow these coding standards:

* **PEP 8**: Python code style guide
* **Type Hints**: All functions should include type hints
* **Docstrings**: All public functions need docstrings in Google style

### Code Quality Tools

We use the following tools to maintain code quality:

* **Black**: Code formatting
* **isort**: Import sorting
* **flake8**: Linting
* **mypy**: Type checking
* **pytest**: Testing

### Running Quality Checks

```bash
# Format code
black .
isort .

# Run linting
flake8 .

# Type checking
mypy .

# Run tests
pytest
```

Making Changes
--------------

### Workflow

1. **Create a branch**: Create a feature branch for your changes
2. **Make changes**: Implement your feature or fix
3. **Add tests**: Ensure your changes are tested
4. **Update docs**: Update documentation if needed
5. **Submit PR**: Create a pull request

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add new authentication method
fix: resolve issue with data parsing
docs: update installation instructions
test: add tests for edge cases
```

### Testing

Write tests for new features and bug fixes:

```python
import pytest
from your_package import YourClass

def test_your_feature():
    obj = YourClass()
    result = obj.your_method()
    assert result == expected_value
```

Documentation
-------------

### Building Docs Locally

To build and preview documentation changes:

```bash
cd docs/
make html
make serve  # Opens browser to http://localhost:8000
```

### Writing Documentation

* Use clear, concise language
* Include code examples
* Add cross-references using Sphinx directives
* Test all code examples

Reporting Issues
----------------

When reporting bugs or requesting features:

1. **Search existing issues** first
2. **Use issue templates** when available
3. **Provide minimal reproduction** for bugs
4. **Include system information** (OS, Python version, etc.)

### Bug Report Template

```
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Step one
2. Step two
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g., Ubuntu 20.04]
- Python: [e.g., 3.9.0]
- Package Version: [e.g., 1.2.3]
```

Getting Help
------------

If you need help:

* **Documentation**: Check the existing docs first
* **Discussions**: Use GitHub Discussions for questions
* **Issues**: Create an issue for bugs or feature requests
* **Discord/Slack**: Join our community chat (if available)
