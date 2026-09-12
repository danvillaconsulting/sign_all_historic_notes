from pathlib import Path
import tomllib

pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
with pyproject.open("rb") as f:
    release = tomllib.load(f)["project"]["version"]

project = "sign_all_historic_notes"
author = "danvillaconsulting"

extensions = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
