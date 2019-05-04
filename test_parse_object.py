from pprint import pprint
from string import printable
from parse_object import parse


def test_list():
    data = [4, 5, 6]
    actual = parse(data)
    expected = [
        {"parent_path": "/", "path": "/0/", "value": 4},
        {"parent_path": "/", "path": "/1/", "value": 5},
        {"parent_path": "/", "path": "/2/", "value": 6},
    ]
    assert actual == expected


def test_dict():
    data = {"aaa": "bbb", "ccc": "ddd"}
    actual = parse(data)
    expected = [
        {"parent_path": "/", "path": "/aaa/", "value": "bbb"},
        {"parent_path": "/", "path": "/ccc/", "value": "ddd"},
    ]
    assert actual == expected


def test_nested_dict():
    data = {"aaa": {"bbb": "ccc", "ddd": "eee"}, "fff": "ggg"}
    actual = parse(data)
    expected = [
        {"parent_path": "/", "path": "/aaa/"},
        {"parent_path": "/aaa/", "path": "/aaa/bbb/", "value": "ccc"},
        {"parent_path": "/aaa/", "path": "/aaa/ddd/", "value": "eee"},
        {"parent_path": "/", "path": "/fff/", "value": "ggg"},
    ]
    assert actual == expected


def test_dict_list_combo():
    data = {
        "aaa": {
            "bbb": "ccc",
            "something": [
                {"ddd1": "eee1"},
                {"ddd2": "eee2"},
                {"ddd3": "eee3"},
                {"ddd4": "eee4"},
                {"ddd5": "eee5"},
            ],
        },
        "fff": "ggg",
    }
    actual = parse(data)
    expected = [
        {"parent_path": "/", "path": "/aaa/"},
        {"parent_path": "/aaa/", "path": "/aaa/bbb/", "value": "ccc"},
        {"parent_path": "/aaa/", "path": "/aaa/something/"},
        {"parent_path": "/aaa/something/", "path": "/aaa/something/0/"},
        {
            "parent_path": "/aaa/something/0/",
            "path": "/aaa/something/0/ddd1/",
            "value": "eee1",
        },
        {"parent_path": "/aaa/something/", "path": "/aaa/something/1/"},
        {
            "parent_path": "/aaa/something/1/",
            "path": "/aaa/something/1/ddd2/",
            "value": "eee2",
        },
        {"parent_path": "/aaa/something/", "path": "/aaa/something/2/"},
        {
            "parent_path": "/aaa/something/2/",
            "path": "/aaa/something/2/ddd3/",
            "value": "eee3",
        },
        {"parent_path": "/aaa/something/", "path": "/aaa/something/3/"},
        {
            "parent_path": "/aaa/something/3/",
            "path": "/aaa/something/3/ddd4/",
            "value": "eee4",
        },
        {"parent_path": "/aaa/something/", "path": "/aaa/something/4/"},
        {
            "parent_path": "/aaa/something/4/",
            "path": "/aaa/something/4/ddd5/",
            "value": "eee5",
        },
        {"parent_path": "/", "path": "/fff/", "value": "ggg"},
    ]
    assert actual == expected
