from pprint import pprint


def add_parent_path(gen, path):
    for temp in gen:
        if "parent_path" not in temp:
            temp["parent_path"] = path
        yield temp


def walk_tree(data, path):
    if isinstance(data, list):
        yield {"path": path}
        for i, e in enumerate(data):
            gen = walk_tree(e, f"{path}{i}/")
            yield from add_parent_path(gen, path)

    elif isinstance(data, dict):
        yield {"path": path}
        for k, v in data.items():
            gen = walk_tree(v, f"{path}{k}/")
            yield from add_parent_path(gen, path)

    else:
        yield {"path": path, "value": data}


def parse(t):
    out = []
    for e in walk_tree(data=t, path="/"):
        if e["path"] == "/" and "value" not in e:
            continue

        if "parent_path" not in e:
            e["parent_path"] = "/"

        out.append(e)
    return out
