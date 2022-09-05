"""Example application."""
import logging


def execute(vm=None, args=None, config=None) -> int:
    """An example application.

    This function performs a basic thing that does stuff.
    """
    logger = logging.getLogger(__name__)

    print("Flee!! Yellowbeard cometh!")

    logger.info("completed.")
    return 0
