# Q1
def foo():
    a = 0
    if a < 10:
        print("Hello")
        yield a
        print("World")

for i in foo():
    print(i)

# Q2
def foo():
    a = 0
    while a < 10:
        yield a
        a += 1

print(list(foo()))

# Q3
def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen: 
    ...     print(i)
    16
    8
    4
    2
    1
    """
    yield n
    if n == 1:
        pass
    elif n % 2 == 0:
        yield from hailstone_sequence(n // 2)
    else:
        yield from hailstone_sequence(3*n+1)

# Q4
class Tree:
    def __init__(self, label, branches=None):
        self.label = label
        if branches is None:
            branches = []
        assert isinstance(branches, list)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t))
    [1, 2, 5, 3, 4]
    """
    yield t.label
    if not t.is_leaf():
        for b in t.branches:
            yield from tree_sequence(b)


# Challenge Question
def all_paths(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(all_paths(t)))
    [[1, 2, 5], [1, 3, 4]]
    """
    if t.is_leaf():
        yield [t.label]
    for b in t.branches:
        for path in all_paths(b):
            yield [t.label] + path
