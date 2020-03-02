def ensure_consistency(fn):
    """Returns a function that calls fn on its arguments, return fn's return
    value, and returns None if fn's return value is different from any of 
    its previous return values for those same argument.
    Also returns None if more than 20 calls are made.

    >>> def consistent(x):
    ...     return x
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    ...     return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    None
    >>> b(6)
    7
    """
    n = 0
    z = {}
    def helper(x):
        nonlocal n
        n += 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if [val] == z[x]:
            return val
        else:
            z[x] = None
            return None
    return helper


a = ensure_consistency(lambda x:x)
print(a(5))
print(a(5))
print(a(6))
print(a(6))
lst = [1, 2, 3]
b = ensure_consistency(lambda x:x+lst.pop())
print(b(5))
print(b(5))
print(b(6))
