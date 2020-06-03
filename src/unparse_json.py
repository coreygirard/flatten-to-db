from src import unparse_object
import json


def unparse(data):
    data = unparse_object(data)
    return json.dumps(data)
