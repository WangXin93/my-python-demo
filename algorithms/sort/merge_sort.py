"""
Steps:
1. Split the array into 2 arrays
2. Merge sort each array
3. Merge two sorted array

Complexity:

Time: O(N log(N))
Space: O(N) with aux array, can be quicker
"""


def merge(l, r):
    if len(l) == 0:
        return r
    elif len(r) == 0:
        return l
    elif l[0] < r[0]:
        return [l[0]] + merge(l[1:], r)
    else:
        return [r[0]] + merge(l, r[1:])


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[0:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


if __name__ == "__main__":
    lst = [3, 0, 1, 7, 9, 2]
    lst = merge_sort(lst)
    print(lst)
