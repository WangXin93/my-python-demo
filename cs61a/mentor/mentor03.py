# Q1
a = [1, 2]
a.append([3, 4])
print(a)

b = list(a)
a[0] = 5
a[2][0] = 6
print(b)

a.extend([7])
a += [8]
# a += 9
print(a)

b[2][1] = a[2:]
print(a[2][1][0][0])

# Q2
a = [1, 2, [3]]
def mystery(s, t):
    s.pop(1)
    return t.append(s)
b = a
a += [b[0]]
a = mystery(b, a[1:])

# Q3
def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """
    prev = 0
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            inside = accumulate(lst[i])
            prev = inside + prev
        else:
            prev = lst[i] + prev
            lst[i] = prev
    return lst[-1]

# Q4
eggplant = 8
def vegetable(kale):
    def eggplant(spinach):
        nonlocal eggplant
        nonlocal kale
        kale = 9
        eggplant = spinach
        print(eggplant, kale)
    eggplant(kale)
    return eggplant

spinach = vegetable('kale')

# Q5
def has_seven(k):
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def make_pingpong_tracker():
    """Returns a function that returns the next value in the
    pintpong sequence each time it is called.
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ...     output.append(x())
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    """
    index, current, add = 1, 0, True
    def pingpong_tracker():
        nonlocal add, current, index
        if add:
            current += 1
        else:
            current -= 1
        if has_seven(current):
            add = not add
        index += 1
        return current
    return pingpong_tracker