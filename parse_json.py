import parse_object
import json


def parse(data):
    return parse_object.parse(json.loads(data))
