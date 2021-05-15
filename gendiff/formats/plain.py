# -*- coding:utf-8 -*-


def format_plain(dic, addon='', lines=''):
    start = "Property '" + addon
    ldic = list(dic)
    for key in ldic:
        value = dic.get(key)
        if value[0] == 'deleted':
            lines += f"{start}{key}' was removed\n"
        if value[0] == 'added':
            if isinstance(value[1], dict):
                finish = "[complex value]"
            else:
                finish = f"{format_value(value[1])}"
            lines += f"{start}{key}' was added with value: {finish}\n"
        if value[0] == 'changeddict' or value[0] == 'changed':
            if isinstance(value[-1], dict):
                lines = format_plain(value[-1], addon+key+'.', lines)
            else:
                lines += f"{start}{key}' was updated. From {format_value(value[1])} to {format_value(value[2])}\n"  # noqa: E501
    return lines


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'{0}'".format(value)
    elif value == {'key': 'value'}:
        value = '[complex value]'
    return value
