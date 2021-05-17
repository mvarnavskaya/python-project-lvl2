from gendiff import generate_diff


answer = u'''{"follow": ["deleted", false], "host": ["unchanged", "hexlet.io"], "proxy": ["deleted", "123.234.53.22"], "timeout": ["changed", 50, 20], "verbose": ["added", true]}'''


def test_flat_json():
    a = answer
    b = generate_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json',
        'json'
    )
    assert len(a) == len(b)
