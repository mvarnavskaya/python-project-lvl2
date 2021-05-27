#!/usr/bin/env python
import argparse


DEFAULT_STYLE = 'stylish'


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format_name',
        default=DEFAULT_STYLE,
        help="set format of output (default: '{0}')".format(DEFAULT_STYLE)
    )
    args = parser.parse_args()
    return args
