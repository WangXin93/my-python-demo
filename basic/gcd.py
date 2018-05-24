def gcd(m, n):
    """Returns the largest k that divides both n and m.
    Using Euclidean algorithm.
    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

    k, m, n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(5, 5)
    5
    """
    if m == n:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m - n, n)
