from hypothesis.strategies import (
    booleans,
    dictionaries,
    floats,
    lists,
    none,
    recursive,
    text,
    composite,
)
from hypothesis import assume
from string import printable
import json


printable_without_slash = "".join(c for c in printable if c != "/")
_json_strategy = recursive(
    none() | booleans() | floats() | text(printable_without_slash),
    lambda children: lists(children, 1)
    | dictionaries(text(printable_without_slash), children, min_size=1),
)


@composite
def json_strategy(draw):
    example = draw(_json_strategy)
    s = json.dumps(example)
    # assume("/" not in s)
    return s
