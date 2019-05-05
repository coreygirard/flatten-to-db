from ruamel.yaml import YAML
from pprint import pprint
from functools import partial

y = """
# example
# example 2
name:
  # details
  family: Smith   # aaa
  given: John  # bbb
  # ccc
"""

# temp._yaml_comment.comment[1][0].value
"# example\n"

# temp._yaml_comment.comment[1][1].value
"# example 2\n"

# temp['name']._yaml_comment.comment[1][0].value
"# details\n"

# temp['name']._yaml_comment._items['family'][2].value
"# aaa\n"

# temp['name']._yaml_comment._items['given'][2].value
"# bbb\n"


def strip_nones(d):
    a = []
    for e in d:
        if e is None:
            pass
        elif isinstance(e, list):
            a.extend(strip_nones(e))
        else:
            a.append(e.value)
    return a


def walk_tree(data, parent_path, path):
    comments = []
    try:
        comments.extend(strip_nones(data._yaml_comment.comment))
    except:
        pass
    """
    try:
        comments.extend(strip_nones(data._yaml_comment._items.values()))
    except:
        pass
    """

    if isinstance(data, list):
        yield {"parent_path": parent_path, "path": path, "comments": comments}
        for i, e in enumerate(data):
            yield from walk_tree(e, path, f"{path}{i}/")

    elif isinstance(data, dict):
        yield {"parent_path": parent_path, "path": path, "comments": comments}
        for k, v in data.items():
            for temp in walk_tree(v, path, f"{path}{k}/"):
                temp.setdefault("comments", strip_nones(data._yaml_comment.items[k]))
                yield temp

    else:
        temp = {"parent_path": parent_path, "path": path, "value": data}
        if comments != []:
            temp["comments"] = comments
        yield temp


def _parse(data):
    gen = walk_tree(data=data, parent_path="/", path="/")
    return list(gen)
    """
    gen = filter(lambda d: d["path"] != "/" or "value" in d, gen)

    def f(d):
        if "parent_path" not in d:
            d["parent_path"] = "/"
        return d

    gen = map(f, gen)

    return list(gen)
    """


def parse(data=None, filename=None, comments=True):
    if (data is not None and filename is not None) or (
        data is None and filename is None
    ):
        raise TypeError("Pass either data or filename, but not both")

    yaml = YAML(typ="rt")

    if data is not None:
        y = yaml.load(data)
    else:
        with open(filename, "r") as f:
            y = yaml.load(f)

    result = _parse(y)
    if not comments:
        for d in result:
            d.pop("comments")

    return result
