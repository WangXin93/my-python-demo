class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert isinstance(rest, Link) or rest is Link.empty
        self.first = first
        self.rest = rest

    def __repr__(self):
        if not self.rest:
            s = 'Link({})'.format(self.first)
        else:
            s = 'Link({}, {})'.format(self.first, str(self.rest))
        return s

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest:
        return lnk.first + sum_nums(lnk.rest)
    else:
        return lnk.first

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    firsts = [i.first for i in lst_of_lnks]
    rests = [i.rest for i in lst_of_lnks]
    if all(rests):
        rest = multiply_lnks(rests)
    else:
        rest = Link.empty
    def mul(lst):
        start = 1
        for i in lst:
            start = start * i
        return start
    return Link(mul(firsts), rest)

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >>> lnk
    Link(1, Link(5))
    """
    if not lnk.rest:
        return lnk
    elif lnk.first != lnk.second:
        return lnk
    elif lnk.first == lnk.second:
        lnk.rest = lnk.rest.rest

    if lnk.rest:
        remove_duplicates(lnk)

    return lnk


# Midterm review
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*n for i,n in enumerate(lst) if i%2==0]


def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    >>> quicksort_list([2, 3, 5, 1, 6])
    [1, 2, 3, 5, 6]
    """
    if len(lst) == 1 or len(lst) == 0:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return less + [pivot] + greater


def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(max_product(lst[2:])*lst[0],
                   max_product(lst[3:])*lst[1])

class tree:
    empty = []
    def __init__(self, label, branches=empty):
        for b in branches:
            assert isinstance(b, tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.is_leaf():
            return 'tree({})'.format(self.label)
        else:
            branches_str = ', '.join(repr(b) for b in self.branches)
            return 'tree({}, [{}])'.format(self.label, branches_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k+1):
                indented.append('  ' + line)
        return [str(self.label)] + indented


from functools import reduce
from operator import add, mul
def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if isinstance(tree.label, int):
        return tree.label
    else:
        labels = [eval_tree(b) for b in tree.branches]
        ops = {'*': mul, '+': add}
        return reduce(ops[tree.label], labels)


def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = tree(1, [tree(1), tree(2, [tree(1, [tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x:f(f(x))
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t
