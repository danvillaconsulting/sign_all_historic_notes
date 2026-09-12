"""CLI entrypoint for sign_all_historic_notes."""

import rich_click as click


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
def main() -> None:
    """Sign all historic notes."""
    click.echo("sign_all_historic_notes is ready.")


if __name__ == "__main__":
    main()
