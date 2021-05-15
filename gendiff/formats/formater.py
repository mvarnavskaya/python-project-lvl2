# -*- coding:utf-8 -*-

from gendiff.formats.json import format_json
from gendiff.formats.plain import format_plain
from gendiff.formats.stylish import format_stylish

FORMATERS = {  # noqa:WPS407
    'json': format_json,
    'plain': format_plain,
    'stylish': format_stylish,
}
DEFAULT_STYLE = 'stylish'


def call_formater(diff, style=DEFAULT_STYLE):
    style = FORMATERS.get(style)
    if style is not None:
        return style(diff)
