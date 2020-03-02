# Q1
x, y, z = 1, 2, 3
y = [x, [y, [z, []]]]
x = [2, y, y[1][1][1]]
z = 0

# Q2
# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
    

t = tree(5, [
    tree(1, [
        tree(7, [
            tree(4, [
                tree(3)
            ])
        ]),
        tree(2)
    ]),
    tree(2, [
        tree(0),
        tree(9)
    ])
])

def sum_range(t):
    """Returns the range of the sums of t, that is, the difference
    between the largest and the smallest sums of t.

    >>> sum_range(t)
    13
    """
    def helper(t):
        if is_leaf(t):
            return (label(t), label(t))
        else:
            a = min([helper(b)[1] for b in branches(t)])
            b = max([helper(b)[0] for b in branches(t)])
            x = label(t)
            return (b+x, a+x)
    x, y = helper(t)
    return x - y
    
# Q2.2
def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not
    contain 1 after 1.

    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven(n - 1), no_eleven(n - 2)
        return [[6]+s for s in a] + [[1, 6]+s for s in b]

# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = tree('+', [tree(2), tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = tree('*', [tree(2), tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = tree('*', [tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(tree('*'))
    1
    """
    if label(t) == '+':
        return sum(eval_with_add(b) for b in branches(t))
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for _ in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return label(t)
