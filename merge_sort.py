"""
On input of n elements:
    If n<2:
        Return.
    else:
        Sort left half of elements.
        Sort right half of elements.
        Merge sorted halves.

For example:

4 2 6 8 1 3 7 5 # divide
4 2 6 8    1 3 7 5
4 2    6 8    1 3    7 5
4   2   6   8   1   3   7   5 # start merge_
2 4    6 8    1 3    5 7                    |
2 4 6 8    1 3 5 7                          > call stack have depth log(n)
1 2 3 4 5 6 7 8                            _|
each layer have n operations.
so merge sort do nlog(n) running times.
"""
import random
import unittest

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        left_arr = merge_sort(arr[:len(arr)//2])
        right_arr = merge_sort(arr[len(arr)//2:])
        # Merge
        i,j,k = 0,0,0 # i left counter, j right counter, k master counter.
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
        return arr 

class test_mergesort(unittest.TestCase):
    def test_mergesort(self):
        test = list(range(1, 100))
        random.shuffle(test)
        self.assertEqual(merge_sort(test), sorted(test))

if __name__ == "__main__":
    unittest.main()
