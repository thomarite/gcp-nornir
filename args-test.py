import ipdb
import argparse
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_cli


_version = '0.0.1'

def parse_args():
    parser = argparse.ArgumentParser(description="FRR TI-LFA show commands")
    parser.add_argument(
        '-f', '--file', help='save output to file', nargs='?', default=None, const='output-show-frr-napalm.txt')
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s (version {})'.format( _version))
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.file:
        print(args.file)


if __name__ == "__main__":
    main()
