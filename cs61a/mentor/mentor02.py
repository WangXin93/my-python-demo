# Q1
a = [1, 2, 3]
b = a
a = a + [4, 5]
c = a
a = [4, 5]
d = c[0:2]
c[0] = 9

# Q2
def reverse(lst):
    if len(lst) <= 1:
        return lst
    return reverse(lst[1:]) + [lst[0]]

lst = [1, [2, 3], 4]
rev = reverse(lst)

# Q3
def all_primes(nums):
    """
    Takes in a list nums and returns a new list only the
    primes from nums

    >>> all_primes([1, 3, 9, 12])
    [3]
    """
    return [i for i in nums if is_prime(i)]

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Q4
def list_of_lists(lst):
    """
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2]]

    >>> list_of_lists([1])
    [[0]]

    >>> list_of_lists([])
    []
    """
    return [list(range(i)) for i in lst]

# Q5
def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

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

t = tree(9,[
    tree(2),
    tree(4, [
        tree(1)
    ]),
    tree(4, [
        tree(7),
        tree(3)
    ])])

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def sum_of_nodes(t):
    """
    >>> sum_of_nodes(t)
    30
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + sum(sum_of_nodes(b) for b in branches(t))