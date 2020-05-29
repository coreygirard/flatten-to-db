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
_object_strategy = recursive(
    none() | booleans() | floats() | text(printable_without_slash),
    lambda children: lists(children, 1)
    | dictionaries(text(printable_without_slash), children, min_size=1),
)


@composite
def object_strategy(draw):
    example = draw(_object_strategy)
    # assume("/" not in json.dumps(example))
    return example
