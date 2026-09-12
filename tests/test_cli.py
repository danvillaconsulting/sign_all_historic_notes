from importlib.metadata import entry_points
from pathlib import Path
import tomllib
from click.testing import CliRunner

from sign_all_historic_notes.cli import main


def test_cli_help_shows_command_description() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "Sign all historic notes." in result.output


def test_cli_short_help_alias_works() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["-h"])

    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_cli_runs() -> None:
    runner = CliRunner()
    result = runner.invoke(main)

    assert result.exit_code == 0
    assert "sign_all_historic_notes is ready." in result.output


def test_console_script_entrypoint_name() -> None:
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with pyproject.open("rb") as f:
        config = tomllib.load(f)
    assert config["project"]["scripts"]["sign-all-historic-notes"] == "sign_all_historic_notes.cli:main"

    scripts = entry_points(group="console_scripts")
    script = next((ep for ep in scripts if ep.name == "sign-all-historic-notes"), None)
    assert script is not None
    assert script.value == "sign_all_historic_notes.cli:main"
