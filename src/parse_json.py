from src import parse_object
import json


def parse_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return parse_object.parse(data)


def parse(data):
    data = json.loads(data)
    return parse_object.parse(data)
