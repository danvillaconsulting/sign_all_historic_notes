# sign_all_historic_notes

Minimal Python scaffold with:
- `pyproject.toml`-based install
- `rich-click` CLI entry point
- Sphinx docs skeleton

## Quickstart

```bash
pip install -e ".[test,dev]"
sign-all-historic-notes --help
pytest
```

For test-only environments:

```bash
pip install -e ".[test]"
pytest
```