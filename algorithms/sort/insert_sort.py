""" Insert sort
Steps:

1. Find the smallest item in the list
2. swap the smallest item to the front and fix it.
3. Execuate step 1 with the remainingg list util the list is empty

Complexity:

Suppose there are N items in the list. Find the smallest item need N times.
There are N times find smallest operation. Totally there are O(N^2) complexity.

The space complexity is constant, i.e., O(1) complexity.
"""


def insert_sort(lst):
    front = 0
    while front < len(lst):
        # Find the smallest item
        min_pos = front
        min_val = lst[front]
        for i in range(front, len(lst)):
            if lst[i] < min_val:
                min_val = lst[i]
                min_pos = i

        # Swap the smallest item to the front
        temp = lst[front]
        lst[front] = lst[min_pos]
        lst[min_pos] = temp

        # Find the smallest item for the remaining lst
        front += 1


if __name__ == "__main__":
    lst = [3, 0, 1, 7, 9, 2]
    insert_sort(lst)
    print(lst)
