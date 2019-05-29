from hypothesis.strategies import (
    booleans,
    composite,
    dictionaries,
    floats,
    integers,
    just,
    lists,
    one_of,
    sampled_from,
    sets,
    text,
    tuples,
)
from hypothesis import assume

from string import ascii_lowercase
import json


@composite
def tag_name_strategy(draw):
    return draw(text(ascii_lowercase, min_size=1, max_size=1))


@composite
def attribute_key_strategy(draw):
    return draw(text(ascii_lowercase, min_size=1, max_size=1))


@composite
def attribute_value_strategy(draw):
    return '"' + draw(text(ascii_lowercase, min_size=1, max_size=1)) + '"'


@composite
def attributes_strategy(draw):
    out = []
    keys = attribute_key_strategy()
    values = attribute_value_strategy()
    for k, v in draw(dictionaries(keys, values, max_size=5)).items():
        out.append((k, v))
    return out


@composite
def element_contents_strategy(draw):
    return draw(lists(element_strategy(), max_size=3))


@composite
def element_strategy(draw):
    return {
        "tag": str(draw(tag_name_strategy())),
        "attributes": draw(attributes_strategy()),
        "contents": draw(element_contents_strategy()),
    }


@composite
def xml_strategy(draw):
    temp = draw(element_strategy())
    assume(len(json.dumps(temp)) < 10000)
    return temp


def to_xml_string(data):
    attributes = " ".join(f"{k}={v}" for k, v in data["attributes"])
    if attributes:
        start = f"<{data['tag']} {attributes}>"
    else:
        start = f"<{data['tag']}>"
    contents = "".join(to_xml_string(e) for e in data["contents"])
    end = f'</{data["tag"]}>'
    return start + contents + end


@composite
def before_and_after(draw):
    before = draw(xml_strategy())
    after = to_xml_string(before)
    return before, after


from pprint import pprint

strat = before_and_after()
for _ in range(20):
    before, after = strat.example()

    print("-" * 20)
    pprint(before)
    print()
    pprint(after)
