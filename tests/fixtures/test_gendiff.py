import json

from gendiff import generate_diff


def test_flat_json():
    a = json.load(open('./tests/fixtures/diff_file1_file2.json'))
    b = generate_diff.get_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json'
    )

    assert len(a.read()) == len(b)
