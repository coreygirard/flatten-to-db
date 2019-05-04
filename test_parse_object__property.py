from pprint import pprint
from collections import Counter
from hypothesis import given


from parse_json import parse
from strategy_json import json_strategy


@given(json_strategy)
def test_doesnt_fail(j):
    parse(j)


@given(json_strategy)
def test_is_list_of_maps(j):
    out = parse(j)
    assert isinstance(out, list)
    for e in out:
        assert isinstance(e, dict)
        assert "parent_path" in e
        assert "path" in e
        # won't always have 'value', so don't check


@given(json_strategy)
def test_parent_paths_have_counterparts(j):
    out = parse(j)

    paths = Counter(map(lambda d: d["path"], out))
    parent_paths = Counter(map(lambda d: d["parent_path"], out))

    for k, v in parent_paths.items():
        if k == "/":  # the root doesn't link to any parent
            continue

        assert v >= paths[k]


@given(json_strategy)
def test_link_chain_to_root(j):
    out = parse(j)

    pprint(out)
