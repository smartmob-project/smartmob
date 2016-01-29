# -*- coding: utf-8 -*-

import argparse
import pkg_resources
import sys

version = pkg_resources.resource_string('smartmob', 'version.txt')
version = version.decode('utf-8').strip()
"""Package version (as a dotted string)."""

cli = argparse.ArgumentParser(description="Run programs.")
cli.add_argument('--version', action='version', version=version,
                 help="Print version and exit.")

def main(arguments=None):
    """Command-line entry point.

    :param arguments: List of strings that contain the command-line arguments.
       When ``None``, the command-line arguments are looked up in ``sys.argv``
       (``sys.argv[0]`` is ignored).
    :return: This function has no return value.
    :raise SystemExit: The command-line arguments are invalid.
    """

    # Parse command-line arguments.
    if arguments is None:
        arguments = sys.argv[1:]
    arguments = cli.parse_args(arguments)

    # Start the event loop.
    loop = asyncio.get_event_loop()

    # Proceed.
    try:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv[1:]))
