"""
Method1: Brute force

Method2: Newton's method

    x_1 = x0 - \frac{f(x_0)}{f'(x_0)}

Initialize i to x, then iterate:

    i = i - \frac{i^2 - n}{2 \times i}

Method3: Binary Search
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        i = x+1
        def f(i): return i*i - x
        def fprime(i): return 2*i
        while True:
            if (int(i)+1) * (int(i)+1) > x and int(i) * int(i) <= x:
                return int(i)
            y = f(i)
            yprime = fprime(i)
            i = i - y/yprime


if __name__ == "__main__":
    print(Solution().mySqrt(0))
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(3))
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(8))
    print(Solution().mySqrt(9))
