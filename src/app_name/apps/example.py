"""Example application."""
import logging

SUBCOMMAND = "example-command"
"""Override the default subcommand name. Remove if unnecessary."""

ALIASES = ["exc"]
"""Add subcommand aliases."""


def config_args(parser):
    """Add example command line parameters."""
    parser.add_argument("--pillage", help="Pillage in piratey ways.")


def execute(vm=None, args=None, config=None) -> int:
    """An example application.

    This function performs a basic thing that does stuff.
    """
    logger = logging.getLogger(__name__)

    print(f"vm={vm}")
    print("Yay example!")

    logger.info("completed.")
    return 0
