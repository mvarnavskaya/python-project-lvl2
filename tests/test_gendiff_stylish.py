import json

from gendiff import generate_diff

answer = u'''{
    common: {
    + follow: False
      setting1: Value 1
    - setting2: 200
    - setting3: True
    + setting3: None
    + setting4: blah blah
    + setting5: {
        key5: value5
    }
      setting6: {
        doge: {
        - wow: 
        + wow: so much
      }
        key: value
      + ops: vops
    }
  }
    group1: {
    - baz: bas
    + baz: bars
      foo: bar
    - nest: {'key': 'value'}
    + nest: str
  }
  - group2: {
      abc: 12345
      deep: {
        id: 45
    }
  }
  + group3: {
      deep: {
        id: {
          number: 45
      }
    }
      fee: 100500
  }
}'''

def test_genfiff_stylish():
    a = answer
    b = generate_diff(
        './tests/fixtures/file3.json',
        './tests/fixtures/file4.json',
        'stylish'
    )
    assert len(a) == len(b)
