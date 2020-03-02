def longest_increasing_suffix(n):
    """Return the longest increasing suffix of a positive
    integer n.
    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901) # Note: 01 is the suffix, displayed as 1
    1
    """
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if last < m:
            m, suffix, k = last, suffix+last*k, 10*k
        else:
            return suffix
    return suffix


def sandwich(n):
    """Return True if n contains a sandwich and False
    otherwise
    >>> sandwich(416263) # 626
    True
    >>> sandwich(5050) # 505 or 050
    True
    >>> sandwich(4441) # 444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    """
    tens, ones = n % 100 // 10, n % 10
    n = n // 100
    while n:
        if n % 10 == ones:
            return True
        else:
            tens, ones = n % 10, tens
            n = n // 10
    return False


def luhn_sum(n):
    """Return the Luhn sum of n.
    >>> luhn_sum(135) # 1 + 6 + 5
    12
    >>> luhn_sum(185) # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743) # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + (x % 10)
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier
    return total
