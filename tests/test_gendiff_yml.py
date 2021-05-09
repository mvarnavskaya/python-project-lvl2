from gendiff import generate_diff


answer = u'''{
    constant: yep
  - test: bar
  + test: foo
  - foo: bar
  + bar: foo
}'''


def test_flat_yml():
    a = answer
    b = generate_diff.get_diff(
        './tests/fixtures/file1.yml',
        './tests/fixtures/file2.yml'
    )
    assert len(a) == len(b)
