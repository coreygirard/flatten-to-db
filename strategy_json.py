from hypothesis.strategies import (
    booleans,
    dictionaries,
    floats,
    lists,
    none,
    recursive,
    text,
)
from string import printable


json_strategy = recursive(
    none() | booleans() | floats() | text(printable),
    lambda children: lists(children, 1)
    | dictionaries(text(printable), children, min_size=1),
)
