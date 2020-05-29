import xmltodict


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


def _parse(xml):
    data = xmltodict.parse(xml)
    gen = walk_tree(data=data, parent_path="/", path="/", tag="")
    gen = filter(lambda d: d["path"] != "/", gen)

    def f(d):
        if "parent_path" not in d:
            d["parent_path"] = "/"
        return d

    gen = map(f, gen)
    return list(gen)


def parse(data=None, filename=None):
    assert (
        data is None or filename is None
    ), "Pass either data or filename, but not both"

    if filename is not None:
        with open(filename, "r") as f:
            data = f.read()

    return _parse(data)


def unparse_recurse(data, path="/"):
    # TODO: currently relies on proper ordering
    out = {}
    for i, row in enumerate(data):
        if row["parent_path"] == path:
            if row["value"] != "":
                out[row["tag"]] = {"#text": row["value"]}
            else:
                out[row["tag"]] = unparse_recurse(
                    data[i + 1 :], path + row["tag"] + "/"
                )
            for k, v in row["attributes"].items():
                out[row["tag"]]["@" + k] = v
    return out


def unparse(data, header=False):
    tree = unparse_recurse(data)

    return xmltodict.unparse(tree, pretty=True, indent="  ", full_document=header)
