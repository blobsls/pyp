# File: pyp_package/cli.py
# This module will handle the command-line interface.

import argparse
from pyp_package import install, uninstall

def main():
    parser = argparse.ArgumentParser(description='Python Package Manager, Similar to Pip and PyPi')
    parser.add_argument('--package', type=str, help='Name of the package to install or uninstall')
    parser.add_argument('--install', action='store_true', help='Install the specified package')
    parser.add_argument('--uninstall', action='store_true', help='Uninstall the specified package')
    args = parser.parse_args()

    if args.install and args.package:
        install(args.package)
    elif args.uninstall and args.package:
        uninstall(args.package)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
