from src.utils import split_path


def special_cases(tree, path, node):
    if path == []:
        return True, node
    if node == {}:
        return True, tree
    if tree is None:
        return True, tree
    return False, None


def unparse_recurse_helper(tree, path, node):
    flag, value = special_cases(tree, path, node)
    if flag:
        return value

    head, *tail = path
    tree[head] = unparse_recurse_helper(tree.get(head, {}), tail, node)
    return tree


def unparse_recurse(elems):
    out = {}
    for e in elems:
        if "value" not in e:
            continue
        out = unparse_recurse_helper(out, e["split_path"], e["value"])
    return out


def becomes_list(tree):
    return sorted(list(tree.keys())) == list(range(len(tree.keys())))


def create_lists_recurse(tree):
    if not isinstance(tree, dict):
        return tree
    if becomes_list(tree):
        return [create_lists_recurse(tree[k]) for k in sorted(tree.keys())]
    return {k: create_lists_recurse(v) for k, v in tree.items()}


def unparse(data):
    for i, _ in enumerate(data):
        data[i]["split_path"] = split_path(data[i]["path"])
    tree = unparse_recurse(data)
    tree = create_lists_recurse(tree)
    return tree
