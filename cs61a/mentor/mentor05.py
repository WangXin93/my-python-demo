class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __str__(self):
        if is_empty(self.rest):
            return str(self.first)
        else:
            start = str(self.first)
            start += ' -> '
            return start + str(self.rest) 

    def __repr__(self):
        if is_empty(self.rest):
            return 'Link({})'.format(self.first)
        else:
            s = 'Link({}, {})'.format(self.first, repr(self.rest))
            return s

def is_empty(link):
    if link is Link.empty:
        return True

def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4)))) 
    """
    if is_empty(lst):
        return Link.empty
    elif is_empty(lst.rest):
        return Link(lst.first)
    else:
        return Link(lst.first, skip(lst.rest.rest))

def skip_new(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip_new(a)
    >>> b
    None
    >>> a
    Link(1, Link(3))
    """
    if is_empty(lst) or is_empty(lst.rest):
        pass
    else:
        lst.rest = lst.rest.rest
        skip_new(lst.rest)

def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    if is_empty(lst.rest):
        return Link(lst.first)
    else:
        return join_link(reverse(lst.rest), Link(lst.first))

def join_link(l1, l2):
    if is_empty(l1):
        return l2
    else:
        return Link(l1.first, join_link(l1.rest, l2))

# Midterm review
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches

def contains_n(elem, n, t):
    """
    >>> contains = contains_n
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf():
        return n==1 and t.label == elem
    elif t.label == elem:
        return any(contains_n(elem, n-1, b) for b in t.branches)
    else:
        return any(contains_n(elem, n, b) for b in t.branches)

def factor_tree(n):
    for i in range(2, n):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)
