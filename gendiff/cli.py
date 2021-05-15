#!/usr/bin/env python
import argparse


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format_name', help='set format of output')
    args = parser.parse_args()
    return args
