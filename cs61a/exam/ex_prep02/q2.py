def combine(left, right):
    """Return all of LEFT's digits followed by all of
    RIGHT's digits."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the digits of N in reverse.

    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n % 10, reverse(n // 10))

def remove(n, digit):
    """Return all digits of N that are not DIGIT, for 
    DIGIT less than 10.

    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            removed = removed * 10 + last
    return reverse(removed)
