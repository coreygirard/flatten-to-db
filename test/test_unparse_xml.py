from collections import OrderedDict
from pprint import pprint

from src import parse_xml


def test__unparse__dict_list_simple():
    _input = [
        {
            "attributes": {},
            "parent_path": "/",
            "path": "/aaa/",
            "tag": "aaa",
            "value": "",
        },
        {
            "attributes": {"hello": "world"},
            "parent_path": "/aaa/",
            "path": "/aaa/bbb/",
            "tag": "bbb",
            "value": "ccc",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/something/",
            "tag": "something",
            "value": "",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/something/",
            "path": "/aaa/something/ddd1/",
            "tag": "ddd1",
            "value": "eee1",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/something/",
            "path": "/aaa/something/ddd2/",
            "tag": "ddd2",
            "value": "eee2",
        },
        {
            "attributes": {},
            "parent_path": "/aaa/",
            "path": "/aaa/fff/",
            "tag": "fff",
            "value": "ggg",
        },
    ]

    expected = "\n".join(
        [
            "<aaa>",
            '  <bbb hello="world">ccc</bbb>',
            "  <something>",
            "    <ddd1>eee1</ddd1>",
            "    <ddd2>eee2</ddd2>",
            "  </something>",
            "  <fff>ggg</fff>",
            "</aaa>",
        ]
    )

    actual = parse_xml.unparse(_input)
    assert actual == expected
