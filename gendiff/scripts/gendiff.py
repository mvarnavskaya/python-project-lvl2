#!/usr/bin/env python

from gendiff import cli
from gendiff import generate_diff


def main():
    args = cli.run()
    print(generate_diff.starter(args, format='stylish'))


if __name__ == '__main__':
    main()
