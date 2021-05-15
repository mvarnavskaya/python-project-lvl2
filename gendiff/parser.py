#!/usr/bin/env python
import json
import os
import yaml


get_loader = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def read_file(file_path):
    _, ext = os.path.splitext(file_path)
    call_loader = get_loader(ext.lower())
    if call_loader:
        try:
            with open(file_path) as data_file:
                return call_loader(data_file)
        except:
            return "Sorry, our program not supported this format. Try 'Json' or 'Yml'"  # noqa: E501
