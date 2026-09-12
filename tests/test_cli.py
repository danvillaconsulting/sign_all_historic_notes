import shutil
import subprocess

import pytest
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
    executable = shutil.which("sign-all-historic-notes")
    if not executable:
        pytest.skip("Console script is not installed in this environment.")

    result = subprocess.run(
        [executable, "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Sign all historic notes." in result.stdout
