# Installation

## Requirements

- Python 3.9 or higher
- pip (Python package installer)

## Basic Installation

To install the Upassist Python SDK, use pip:

```bash
pip install upassist
```

## Development Installation

If you want to contribute to the SDK or build the documentation locally, install with development dependencies:

```bash
pip install upassist[docs]
```

This will install additional packages required for:
- Building documentation
- Running tests
- Development tools

## Verifying Installation

You can verify the installation by running Python and importing the package:

```python
import upassist
print(upassist.__version__)
```

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade upassist
```

## Uninstalling

To uninstall the package:

```bash
pip uninstall upassist
``` 