
"""
<https://docs.python.org/3/library/heapq.html>
<https://www.youtube.com/watch?v=AEAmgbls8TM&feature=youtu.be>

Steps:

1. Put every item in the list into a heap
2. Each step get the smallest item from the heap, put the smallest into
  a new list
3. Repeat until the heap is empty

```python
from heapq import heappush, heappop
This is the simple version with python module
def heap_sort(lst):
    h = []
    for val in lst:
        heappush(h, val)
    return [heappop(h) for i in range(len(h))]
```

There is also inplace heap sort

Steps:

1. Heapification (Bottom-up heapify the array)
    1. Sink nodes in reverse order, sink(k)
    2. After sinking, guaranteed that tree rooted at position k is a heap
2. Delete the head of the heap, delete the last item from the heap, swap
  the last item in the root, and sink(0)

Time complexity: O(N log(N))
Space complexity: O(1)

The definition of sink(k):

Steps:
1. If k-th item is larger than one of its child, swap it with its child.
  the children of k-th item is the (2*k+1) and (2*k+2).
  (if the item is larger than both of the children, swap with the smaller one)
2. Repeat this until the end of the heap array.

Example:

3, 0, 1, 7, 9, 2

Heapifiy:
         9
     7       2
   3   0   1

Delete head of heap, and sink(0):
         7
     3       2
   1   0

Delete head of heap, and sink(0):
         3
     1       2
   0

Delete head of heap, and sink(0):
         2
     1       0

Delete head of heap, and sink(0):
         1
     0

Delete head of heap, and sink(0):
         0
"""


def heap_sort(lst):

    def sink(start, end):
        """ MaxHeap sink.
        If lst[start] is smaller than its children, sink down till the end.
        """
        left = 2*start + 1
        right = 2*start + 2

        swap_pos = None
        if left <= end:
            if lst[start] < lst[left]:
                if right > end or lst[left] > lst[right]:
                    swap_pos = left
                elif lst[right] > lst[left]:
                    swap_pos = right
            elif right <= end and lst[start] < lst[right]:
                swap_pos = right

        if swap_pos:
            temp = lst[start]
            lst[start] = lst[swap_pos]
            lst[swap_pos] = temp
            sink(swap_pos, end)

    # Bottom-up heapify the array
    for k in range(len(lst)-1, -1, -1):
        sink(k, len(lst)-1)
        print(lst)

    # Delete the head of the heap, delete the last item from the heap, swap
    # the last item in the root, and sink(0)
    for end in range(len(lst) - 1, 0, -1):
        first = lst[0]
        lst[0] = lst[end]
        lst[end] = first
        sink(0, end-1)
        # print(lst)


if __name__ == "__main__":
    lst = [3, 0, 1, 7, 9, 2]
    heap_sort(lst)
    print(lst)
