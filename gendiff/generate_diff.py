#!/usr/bin/env python
from gendiff.formats import call_formater, DEFAULT_STYLE
from gendiff.parser import read_file


def starter(args):
    return get_diff(args.first_file, args.second_file, args.format)


def get_diff(args_first_file, args_second_file, output_format=DEFAULT_STYLE):
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
    bothed = knew & kold
    for key in all_keys:
        if key in deleted:
            diffe[key] = ['deleted', diff(old.get(key), old.get(key)) if isinstance(old.get(key), dict) else old.get(key)]
        if key in added:
            diffe[key] = ['added', diff(new.get(key), new.get(key)) if isinstance(new.get(key), dict) else new.get(key)]
        if key in bothed:
            oldvalue = old.get(key)
            newvalue = new.get(key)
            if oldvalue != newvalue:
                if isinstance(oldvalue, dict) and isinstance(newvalue, dict):
                    diffe[key] = ['changeddict', diff(oldvalue, newvalue)]
                else:
                    diffe[key] = ['changed', diff(oldvalue, newvalue) if isinstance(oldvalue, dict) and isinstance(newvalue, dict) else oldvalue, newvalue]
            else:
                diffe[key] = ['unchanged', diff(oldvalue, oldvalue) if isinstance(oldvalue, dict) else oldvalue]
    return(diffe)
