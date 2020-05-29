"""
Divide two integer without divide operator.

The idea is to use substraction and bit operation. For example:

dividend=10, divisor=3, we have:
10 = 3*2 + 3*1 + 1

dividend=45, divisor=3, we have:
45 = 3*8 + 3*4 + 3*2 + 3*1

Note the multiplier is range from (2 << 3), (2 << 2), (2 << 1), so
so the complexity will be O(log(dividend) log(dividend))

Reference:
https://www.youtube.com/watch?v=htX69j1jf5U
"""


class Solution:
    # This method use long int, not elegant
    def divide_with_long(self, dividend, divisor):
        div = int(dividend / divisor)
        if div < -2**31 or div > 2**31 - 1:
            return 2**31 - 1
        else:
            return div

    # Use bit operation and substraction
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a - b >= 0:
            x = 0
            while a > (b << 1 << x):
                x += 1
            res += (1 << x)
            a -= (b << x)
        if (dividend > 0) == (divisor > 0):
            return res
        else:
            return -res


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(45, 3))
    print(Solution().divide(1, 1))
    print(Solution().divide(2147483647, 1))
