def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.

    >>> from operator import add, mul
    >>> combine(3, mul, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add ,3) # add(6, add(5, add(0, add(2, 3))))
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0)))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n//10, f, f(n%10, result))
