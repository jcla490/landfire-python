"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Landfire."""


if __name__ == "__main__":
    main(prog_name="landfire")  # pragma: no cover
