import json


def walk_tree(data, parent_path, path):
    if isinstance(data, list):
        yield {"parent_path": parent_path, "path": path}
        for i, e in enumerate(data):
            yield from walk_tree(e, path, f"{path}{i}/")

    elif isinstance(data, dict):
        yield {"parent_path": parent_path, "path": path}
        for k, v in data.items():
            yield from walk_tree(v, path, f"{path}{k}/")

    else:
        yield {"parent_path": parent_path, "path": path, "value": data}


def parse(data):
    gen = walk_tree(data=data, parent_path="/", path="/")
    gen = filter(lambda d: d["path"] != "/" or "value" in d, gen)

    def f(d):
        if "parent_path" not in d:
            d["parent_path"] = "/"
        return d

    gen = map(f, gen)

    return list(gen)
