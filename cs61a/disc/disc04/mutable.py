# Q1
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst1 == lst2

lst1 is lst2

lst2 = lst1
lst1.append(4)
lst1

lst2

lst1 = lst2 + [5]
lst1 == lst2

lst1

lst2

lst2 is lst1

# Q2
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    times = lst.count(x)
    for _ in range(times):
        lst.append(el)

# Q3
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    length = len(lst)
    i = 0
    while i < len(lst) // 2:
        lst[i], lst[length-i-1] = lst[length-i-1], lst[i]
        i = i + 1