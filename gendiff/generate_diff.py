#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gendiff.formats import call_formater, DEFAULT_STYLE
from gendiff.parser import read_file


STATUS = 'status'

ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

VALUE = 'value'
UPDATED_VALUE = 'updated_value'


def generate_diff(args_first_file, args_second_file, output_format=DEFAULT_STYLE):  # noqa: E501
    before = read_file(args_first_file)
    after = read_file(args_second_file)
    diffe = diff(before, after)
    return call_formater(diffe, output_format)


def diff(first_data_set, second_data_set):
    diff = {}
    keys_matched = first_data_set.keys() & second_data_set.keys()
    for key in keys_matched:
        diff[key] = compare_keys_matched(
            first_data_set[key], second_data_set[key],
        )
    keys_removed = first_data_set.keys() - second_data_set.keys()
    for key in keys_removed:  # noqa:WPS440
        diff[key] = {STATUS: REMOVED, VALUE: first_data_set[key]}  # noqa:WPS441, E501
    keys_added = second_data_set.keys() - first_data_set.keys()
    for key in keys_added:  # noqa:WPS440
        diff[key] = {STATUS: ADDED, VALUE: second_data_set[key]}  # noqa:WPS441, E501
    return diff


def compare_keys_matched(first_value, second_value):
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        return {STATUS: NESTED, VALUE: diff(first_value, second_value)}
    if first_value == second_value:
        return {STATUS: UNCHANGED, VALUE: first_value}
    return {STATUS: UPDATED, VALUE: first_value, UPDATED_VALUE: second_value}
