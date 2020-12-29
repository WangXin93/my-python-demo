def count_sort(nums):
    count = [0 for _ in range(4)]
    for num in nums:
        count[num-1] += 1
    res = []
    for i, c in enumerate(count):
        for _ in range(c):
            res.append(i+1)
    return res


def lsd_radix_sort(nums):
    pass

def msd_radix_sort(nums):
    pass

def num2lst(num, length):
    lst = []
    while length:
        lst.append(num % 10)
        num = num // 10
        length -= 1
    lst.reverse()
    return lst



if __name__ == '__main__':
    lst = [3, 2, 4, 1, 2, 3, 4, 1]
    print(count_sort(lst))
    lst = [12, 33, 42, 13, 24, 23, 31]
