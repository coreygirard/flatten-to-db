import parse_yaml


def test_parse():
    y = """
# example
# example 2
name:
  # details
  family: Smith   # aaa
  given: John  # bbb
  # ccc
"""

    expected = [
        {"comments": ["# example\n", "# example 2\n"], "parent_path": "/", "path": "/"},
        {"comments": ["# details\n"], "parent_path": "/", "path": "/name/"},
        {
            "comments": ["# aaa\n"],
            "parent_path": "/name/",
            "path": "/name/family/",
            "value": "Smith",
        },
        {
            "comments": ["# bbb\n"],
            "parent_path": "/name/",
            "path": "/name/given/",
            "value": "John",
        },
    ]
    actual = parse_yaml.parse(y)

    assert expected == actual
