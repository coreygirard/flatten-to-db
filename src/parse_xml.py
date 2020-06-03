from pprint import pprint
import xmltodict
from src.utils import split_path


def walk_tree(data, parent_path, path, tag):
    if isinstance(data, list):
        for i, e in enumerate(data):
            yield from walk_tree(e, parent_path, f"{path}{i}/", tag)

    elif isinstance(data, dict):  # covers OrderedDict
        # every key starting with '@' is an attribute
        attributes = {k[1:]: v for k, v in data.items() if k.startswith("@")}
        yield {
            "parent_path": parent_path,
            "path": path,
            "value": data.get("#text", ""),
            "attributes": attributes,
            "tag": tag,
        }
        for k, v in data.items():
            # don't treat text contents or tag attributes as children
            if k == "#text" or k.startswith("@"):
                continue

            yield from walk_tree(v, path, f"{path}{k}/", str(k))

    else:
        yield {
            "parent_path": parent_path,
            "path": path,
            "value": data,
            "attributes": {},
            "tag": tag,
        }


def parse(xml):
    data = xmltodict.parse(xml)
    gen = walk_tree(data=data, parent_path="/", path="/", tag="")
    gen = filter(lambda d: d["path"] != "/", gen)

    def f(d):
        if "parent_path" not in d:
            d["parent_path"] = "/"
        return d

    gen = map(f, gen)
    return list(gen)


def parse_from_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return parse(data)
