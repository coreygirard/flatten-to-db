from pprint import pprint
from collections import Counter
from hypothesis import given, assume

from src.parse_object import parse
from test.strategy_object import object_strategy


@given(object_strategy())
def test_doesnt_fail(j):
    parse(j)


@given(object_strategy())
def test_is_list_of_maps(j):
    out = parse(j)
    assert isinstance(out, list)
    for e in out:
        assert isinstance(e, dict)
        assert "parent_path" in e
        assert "path" in e
        # won't always have 'value', so don't check


@given(object_strategy())
def test_parent_paths_have_counterparts(j):
    out = parse(j)

    paths = Counter(map(lambda d: d["path"], out))
    parent_paths = Counter(map(lambda d: d["parent_path"], out))

    for k, v in parent_paths.items():
        if k == "/":  # the root doesn't link to any parent
            continue

        assert v >= paths[k]


@given(object_strategy())
def test_path_uniqueness(j):
    out = parse(j)
    paths = [d["path"] for d in out]
    assert len(paths) == len(set(paths))


def add_to_tree(tree, path, value):
    if path == []:
        return value

    crumb, *path = path
    if crumb not in tree:
        tree[crumb] = {}
    tree[crumb] = add_to_tree(tree[crumb], path, value)
    return tree


def lists_to_dicts(data):
    if isinstance(data, list):
        return {str(i): lists_to_dicts(e) for i, e in enumerate(data)}
    elif isinstance(data, dict):
        return {k: lists_to_dicts(v) for k, v in enumerate(data)}
    else:
        return data


@given(object_strategy())
def test_can_rebuild(j):
    out = parse(j)

    for e in out:
        e["split_path"] = e["path"].split("/")[1:-1]

    tree = {}
    for e in out:
        if "value" in e:
            tree = add_to_tree(tree, e["split_path"], e["value"])

    assert tree == lists_to_dicts(j)
