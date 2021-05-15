### Hexlet tests and linter status:
[![Actions Status](https://github.com/mvarnavskaya/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/mvarnavskaya/python-project-lvl2/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2d114634f09fc75a5317/maintainability)](https://codeclimate.com/github/mvarnavskaya/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d114634f09fc75a5317/test_coverage)](https://codeclimate.com/github/mvarnavskaya/python-project-lvl2/test_coverage)

## Installation and usage example

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gendiff.

```bash
pip install --user git+https://github.com/mvarnavskaya/python-project-lvl2.git
```

### As CLI util

```bash
?gendiff -h
usage: gendiff [-h] [-f {json,plain,stylish}] first_file second_file

Generate difference of two JSON or YAML files.

positional arguments:
  first_file            first file to compare
  second_file           second file to compare

optional arguments:
  -h, --help            show this help message and exit
  -f {json,plain,stylish}, --format {json,plain,stylish}
                        set output format(default: 'stylish')
```

Installation and usage example

[![asciicast](https://asciinema.org/a/LeZTuhJQyIyWpP0QcsCu0EC3Q.svg)](https://asciinema.org/a/LeZTuhJQyIyWpP0QcsCu0EC3Q?autoplay=1&speed=2&preload=1&size=medium)
