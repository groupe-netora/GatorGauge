""" parse arguments inputted via command line """
import argparse

import defaults


def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--get',
        default=False,
        help="Download the repositories.\nIf not default project or prefix, must use '--project' or '--prefix'",
        action="store_true")

    parser.add_argument('--list',
                        default=".",
                        const="all",
                        nargs='?',
                        help="List the files with the given extension")

    parser.add_argument('--read',
                        default="",
                        help="Read the information in a given file")

    parser.add_argument(
        '--project',
        default=defaults.PROJECT,
        help='GitHub project to scan, default: ' +
        defaults.PROJECT)

    parser.add_argument(
        '--prefix',
        default=defaults.PREFIX,
        help='Prefix on projects to match (default: match all projects)')

    parser.add_argument('--token',
                        default=defaults.TOKEN,
                        help='GitHub API token')

    parser.add_argument(
        '--out',
        default=defaults.OUT,
        help='Destination directory for GitHub clones (default: current directory)')

    args = parser.parse_args()

    return args
