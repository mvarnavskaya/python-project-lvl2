#!/usr/bin/env python
import argparse
from gendiff.generate_diff import generate_diff


def createParser():
    parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    return parser


def main():
    parser = createParser()
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
