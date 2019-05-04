import parse_object
import json


def parse(data=None, filename=None):
    assert (
        data is None or filename is None
    ), "Pass either data or filename, but not both"

    if data is not None:
        data = json.loads(data)
    else:
        with open(filename, "r") as f:
            data = json.load(f)

    return parse_object.parse(data)
