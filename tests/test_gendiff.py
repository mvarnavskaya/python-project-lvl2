import json

from gendiff import generate_diff


answer = u'''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_flat_json():
    a = answer
    b = generate_diff.get_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json'
    )
    print(a)

    print(b)
    assert len(a) == len(b)
