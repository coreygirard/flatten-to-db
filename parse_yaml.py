import yaml
from pprint import pprint


y = """# example
name:
  # details
  family: Smith   # aaa
  given: John  # bbb"""


def _parse(data):
    return data


def parse(data=None, filename=None, unsafe_load=False):
    if (data is not None and filename is not None) or (
        data is None and filename is None
    ):
        raise TypeError("Pass either data or filename, but not both")

    if not isinstance(unsafe_load, bool):
        raise TypeError(
            "'unsafe_load' parameter must be either True or False. Default value is False"
        )

    if unsafe_load:
        loader_function = yaml.load
    else:
        loader_function = yaml.safe_load

    if data:
        y = loader_function(data)
    else:
        with open(filename, "r") as f:
            y = loader_function(f)

    return _parse(y)


p = parse(y)
print(type(p))
pprint(p)
print(yaml.dump(p))
