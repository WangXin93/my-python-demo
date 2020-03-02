from tree import *

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.

    >>> x = tree(1, [tree(2), tree(2), tree(3)])
    >>> y = tree(3, [tree(2), tree(1), tree(2)])
    >>> about_equal(x, y)
    True
    >>> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >>> about_equal(x, z)
    False
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}
        else:
            counts = {}
            for b in branches(t) + [tree(label(t))]:
                for l, c in label_counts(b).items():
                    if l not in counts:
                        counts[l] = 0
                    counts[l] += 1
        return counts
    return label_counts(t1) == label_counts(t2)
