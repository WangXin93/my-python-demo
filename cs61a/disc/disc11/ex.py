# 1.1
cats = [1, 2]
dogs = [cats, cats.append(23), list(cats)]
cats

dogs[1] = list(dogs)
dogs[1]

dogs[0].append(2)
cats

dogs[2].extend([list(cats).pop(0), 3])
# dogs[3]

dogs

# 1.2
def miley(ray):
    def cy():
        def rus(billy):
            nonlocal cy
            cy = lambda: billy + ray
            return [1, billy]
        if len(rus(2)) == 1:
            return [3, 4]
        else:
            return [cy(), 5]
    return cy()[1]
billy = 6
miley(7)

# 2.1
def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if not s1:
        return s2
    elif not s2:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5)
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if not seq:
        return False
    elif k in seq:
        return True
    else:
        return subset_sum(seq[1:], k-seq[0])

# 3.1
class Tree(object):
    def __init__(self, label, branches=None):
        self.label = label
        if branches is None:
            branches = []
        self.branches = branches
    def is_leaf(self):
        return not self.branches

def average(t):
    """Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            b_total, b_count = sum_helper(b)
            total += b_total
            count += b_count
        return total, count
    total, count = sum_helper(t)
    return total / count

# 6.1
from operator import add, mul
def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    start = 0 if f is add else 1
    for i in it:
        start = f(start, i)
        yield start


# 6.2
# def repeated(f):
#     """
#     >>> double = lambda x: 2*x
#     >>> funcs = repeated(double)
#     >>> identity = next(funcs)
#     >>> double = next(funcs)
#     >>> quad = next(funcs)
#     >>> oct = next(funcs)
#     >>> quad(1)
#     4
#     >>> oct(1)
#     8
#     >>> [g(1) for _, g in zip(range(5), repeated(lambda x:2*x))]
#     [1, 2, 4, 8, 16]
#     """
#     g = 0
#     from functools import partial
#     def foo(x, g):
#         for i in range(g):
#             x = f(x)
#         return x
#     while True:
#         yield partial(foo, g=g)
#         g += 1

def repeated(f):
    """
    >>> double = lambda x: 2*x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x:2*x))]
    [1, 2, 4, 8, 16]
    """
    compose = lambda f, g: lambda x: f(g(x))
    curr = lambda x:x
    while True:
        yield curr
        curr = compose(f, curr)
