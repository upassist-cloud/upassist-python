# Release Notes

This section contains the release notes for all versions of the Upassist Python SDK.

## Latest Release

### [v0.0.6](0.0.6.md) - Documentation and Build System Improvements

**Key Features:**
- 📚 Comprehensive API documentation with MkDocs
- 🛠️ Enhanced build system with dynamic version management
- 🔧 Improved code quality tools (ruff, isort, black)
- 🔒 Added security checks and version validation
- 📦 Updated package management and dependencies

[Read full release notes](0.0.6.md)

## Previous Releases

### v0.0.5
- Initial public release
- Basic heartbeat monitoring functionality
- Log management features
- Synchronous and asynchronous API clients
- Type-safe data models with Pydantic

## Version Support

| Version | Status      | Python Versions | Release Date |
|---------|-------------|----------------|--------------|
| 0.0.6   | Current     | ≥3.9           | 2024-03-19   |
| 0.0.5   | Deprecated  | ≥3.9           | 2024-03-18   |

## Upgrade Guide

To upgrade to the latest version:

```bash
pip install --upgrade upassist
```

For development dependencies:
```bash
pip install --upgrade "upassist[docs]"
```

## Release Schedule

The Upassist Python SDK follows semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality
- **PATCH** version for backwards-compatible bug fixes

We aim to release new versions with the following frequency:
- Major releases: As needed for breaking changes
- Minor releases: Every 2-3 months
- Patch releases: As needed for bug fixes

## Contributing

If you find any issues or have suggestions for improvements, please:
1. Check the [existing issues](https://github.com/upassist-cloud/upassist-python/issues)
2. Create a new issue if needed
3. Follow our [contribution guidelines](https://github.com/upassist-cloud/upassist-python/blob/main/CONTRIBUTING.md)

---

For more information, visit [Upassist Cloud](https://upassist.cloud/) 