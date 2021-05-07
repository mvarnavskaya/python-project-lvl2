#!/usr/bin/env python
import json


def starter(args):
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    return get_diff(first_file, second_file)


def get_diff(first_file, second_file):
    res = {}
    first_keys = set(first_file.keys())
    second_keys = set(second_file.keys())
    all_keys = first_keys | second_keys
    added_keys = second_keys - first_keys
    del_keys = first_keys - second_keys
    for key in sorted(all_keys):
        val_first_file = first_file.get(key)
        val_second_file = second_file.get(key)
        if key in added_keys:
            res['+ ' + key] = val_second_file
        elif key in del_keys:
            res['- ' + key] = val_first_file
        else:
            if val_first_file == val_second_file:
                res['  ' + key] = val_first_file
            else:
                res['- ' + key] = val_first_file
                res['+ ' + key] = val_second_file
    return dict_to_str(res)


def dict_to_str(value):
    res = '{' + '\n'
    for key in list(value.keys()):
        res += '  ' + str(key) + ':' + str(value.get(key)) + '\n'
    res += '}'
    return res
