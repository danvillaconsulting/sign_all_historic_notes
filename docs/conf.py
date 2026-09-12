from pathlib import Path
import re

pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject.read_text(), re.MULTILINE)
release = match.group(1) if match else "0.0.0"

project = "sign_all_historic_notes"
author = "danvillaconsulting"

extensions = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
