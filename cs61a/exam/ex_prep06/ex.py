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

def extend(a, b):
    if is_empty(a.rest):
        a.rest = b
        return a
    else:
        a.rest = extend(a.rest, b)
        return a

def reverse_link(a):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> reverse_link(a)
    Link(3, Link(2, Link(1)))
    """
    current = a
    reverse = Link.empty
    while not is_empty(current):
        rest_of_current = current.rest
        current.rest = reverse
        reverse = current
        current = rest_of_current
    return reverse

def conserve_links(a, b):
    """Makes Linked List a share as many Link instances as possible with
    Linked List b.a can use b's i-th Link instance as its i-th Link
    instance if a and b have the same element at position i.
    Should mutate a. b is allowed to be destroyed. Returns the new first
    Link instance of a.

    >>> x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> y = Link(1, Link(9, Link(3, Link(4, Link(9, Link(6))))))
    >>> z = conserve_links(x, y)
    >>> curr_x, curr_z = x, z
    >>> while curr_z is not Link.empty:
    ...     assert curr_z.first == curr_x.first
    ...     curr_x, curr_z = curr_x.rest, curr_z.rest
    >>> assert z == y
    >>> assert z.rest.rest == y.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    """
    if is_empty(a.rest) and is_empty(b.rest):
        if a.first == b.first:
            return b
        else:
            return a
    else:
        if a.first == b.first:
            b.rest = conserve_links(a.rest, b.rest)
            return b
        else:
            a.rest = conserve_links(a.rest, b.rest)
            return a

def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i-1):
        start = start.rest 
    reverse = Link.empty
    current = start.rest 
    for _ in range(j-i):
        tmp = current.rest
        current.rest = reverse
        reverse = current
        current = tmp
    extend(reverse, current)
    start.rest = reverse
