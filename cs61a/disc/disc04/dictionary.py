# Q2
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x) == {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    True
    """
    out = {}
    for e in s:
        if fn(e) not in out:
            out[fn(e)] = [e]
        else:
            out[fn(e)].append(e)
    return out

# Q3
def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for k, v in d.items():
        if v == x:
            d[k] = y
        if type(v) == dict:
            replace_all_deep(v, x, y)
