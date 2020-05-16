"""
<https://realpython.com/binary-search-python/>

Use ``bisect`` module for binary search in python
Iterative version binary search
Recursive version binary search

## Tricks

To avoid overflow in some language, it is safer to use `` mid = left + (left - right) // 2 `` than ``mid = (left + right) // 2`` beacause ``left + right`` could compute a large number than the data type.

If you implement recursive version binary search, take care of the recursion times limitation, which can be checked by``sys.getrecursionlimit()``.

## Extra

* binary search with special compare function
* binary search with duplicated elements
    * find_leftmost_index
    * find_rightmost_index
    * find_all
* binary search for float points
"""

def binary_contains(lst, value):
    """
    >>> binary_contains([0, 1, 2, 4, 6, 7, 8], 3)
    False
    >>> binary_contains([0, 1, 2, 4, 6, 7, 8], 4)
    True
    """
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] > value:
            right = mid - 1
        elif lst[mid] < value:
            left = mid + 1
    return False

def binary_contains_recursive(lst, value):
    """
    >>> binary_contains([0, 1, 2, 4, 6, 7, 8], 3)
    False
    >>> binary_contains([0, 1, 2, 4, 6, 7, 8], 4)
    True
    """
    def _recur(left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] > value:
            return _iter(left, mid-1)
        elif lst[mid] < value:
            return _iter(mid+1, right)
    return _recur(0, len(lst)-1)
