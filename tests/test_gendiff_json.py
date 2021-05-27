from gendiff import generate_diff


answer = u'''{"timeout": {"status": "updated", "value": 50, "updated_value": 20}, "host": {"status": "unchanged", "value": "hexlet.io"}, "follow": {"status": "removed", "value": false}, "proxy": {"status": "removed", "value": "123.234.53.22"}, "verbose": {"status": "added", "value": true}}'''


def test_flat_json():
    a = answer
    b = generate_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        'json'
    )
    assert len(a) == len(b)
