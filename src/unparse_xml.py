from src.utils import split_path
import xmltodict


def unparse_recurse_helper(tree, path, node):
    if path == []:
        return node
    if node == {}:
        return tree
    head, tail = path[0], path[1:]
    if head not in tree:
        tree[head] = {}
    tree[head] = unparse_recurse_helper(tree[head], tail, node)
    return tree


def unparse_recurse(data):
    out = {}
    for path, node in data:
        out = unparse_recurse_helper(out, path, node)
    return out


def fuse_data(d):
    out = {}
    for k, v in d["attributes"].items():
        out["@" + k] = v
    if d["value"] != "":
        out["#text"] = d["value"]
    return out


def unparse_preprocess(elems):
    out = []
    for e in elems:
        out.append([split_path(e["path"]), fuse_data(e)])
    return out


def create_lists_recurse(tree):
    if not isinstance(tree, dict):
        return tree
    if all(isinstance(k, int) for k in tree.keys()):
        return [create_lists_recurse(tree[k]) for k in sorted(tree.keys())]
    return {k: create_lists_recurse(v) for k, v in tree.items()}


def unparse(data, header=False):
    data = unparse_preprocess(data)
    tree = unparse_recurse(data)
    tree = create_lists_recurse(tree)

    out = xmltodict.unparse(tree, pretty=True, indent="  ", full_document=header)
    return out
