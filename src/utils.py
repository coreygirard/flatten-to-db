def split_path(s):
    out = []
    for e in s.split("/")[1:-1]:  # to lose initial and ending empty strings
        try:
            out.append(int(e))
        except:
            out.append(e)
    return out
