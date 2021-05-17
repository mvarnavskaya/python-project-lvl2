#!/usr/bin/env python
from gendiff.formats import call_formater, DEFAULT_STYLE
from gendiff.parser import read_file


def starter(args):
    return get_diff(args.first_file, args.second_file, args.format_name)


def generate_diff(args_first_file, args_second_file, output_format=DEFAULT_STYLE):
    before = read_file(args_first_file)
    after = read_file(args_second_file)
    diffe = diff(before, after)
    return call_formater(diffe, output_format)


def diff(old, new):
    diffe = {}
    kold = old.keys()
    knew = new.keys()
    all_keys = list(set(kold) | set(knew))
    all_keys.sort()
    deleted = kold - knew
    added = knew - kold
    for key in all_keys:
        oldvalue = old.get(key)
        newvalue = new.get(key)
        if key in deleted:
            value = diff(oldvalue, oldvalue) if is_dict(oldvalue) else oldvalue
            diffe[key] = ['deleted', value]
        elif key in added:
            value = diff(newvalue, newvalue) if is_dict(newvalue) else newvalue
            diffe[key] = ['added', value]
        else:
            if oldvalue != newvalue:
                if isinstance(oldvalue, dict) and isinstance(newvalue, dict):
                    diffe[key] = ['changeddict', diff(oldvalue, newvalue)]
                else:
                    diffe[key] = ['changed', oldvalue, newvalue]
            else:
                value = diff(oldvalue, oldvalue) if is_dict(oldvalue) else oldvalue   # noqa: E501
                diffe[key] = ['unchanged', value]
    return(diffe)


def is_dict(value):
    if isinstance(value, dict):
        return True
    return False
