from tree import tree, label, branches, is_leaf

# An example tree
t = tree(1,
         [tree(3,
               [tree(4),
                tree(5),
                tree(6)]),
          tree(2)])


def tree_max(t):
    """Return the max of a tree.

    >>> tree_max(t)
    6
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)] + [tree_max(b) for b in branches(t)])


def height(t):
    """Return the height of a tree.

    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t.
    >>> square_tree(t)
    [1, [9, [16], [25], [36]], [4]]
    """
    def square(n):
        return n * n
    return tree(square(label(t)), [square_tree(b) for b in branches(t)])


# Another example tree
t2 = tree(2,
         [tree(7,
               [tree(3),
                tree(6,
                     [tree(5),
                      tree(11)])]),
          tree(15)])


def find_path(tree, x):
    """
    >>> find_path(t2, 5)
    [2, 7, 6, 5]
    >>> find_path(t2, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        paths = find_path(b, x)
        if paths:
            return [label(tree)] + paths


def prune(t, k):
    """
    >>> prune(t2, 2)
    [2, [7, [3], [6]], [15]]
    """
    if k == 0:
        return tree(label(t))
    else:
        return tree(label(t), [prune(b, k-1) for b in branches(t)])
