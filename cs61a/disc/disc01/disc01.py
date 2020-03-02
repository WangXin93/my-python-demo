def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp<60 or raining


def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    Move to Section 2: 1
    >>> handle_overflow(20, 32)
    Move to Section 1: 10
    >>> handle_overflow(35, 30)
    No space left in either section
    """
    if s1 <= 30 and s2 <= 30:
        print('No overflow')
    elif s1 > 30 and s2 < 30:
        print('Move to Section 2: {}'.format(30-s2))
    elif s1 < 30 and s2 > 30:
        print('Move to Section 1: {}'.format(30-s1))
    else:
        print('No space left in either section')


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1: return False
    current = 2
    while current < n:
        if n % current == 0:
            return False
        current += 1
    return True


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i<=n:
        if cond(i):
            print(i)
        i += 1


def outer(n):
    def inner(m):
        return n - m
    return inner


def keep_ints_c(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True. currying
    version.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints_c(5)(is_even)
    2
    4
    """
    def inner(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return inner

a = 1
def b(b):
    return a + b
a = b(a)
a = b(a)


from operator import add
def sub(a, b):
    sub = add
    return a - b
add = sub
sub = min
print(add(2, sub(2, 3)))
