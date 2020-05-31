class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        sign = 1 if n > 0 else -1
        n = abs(n)
        while n > 0:
            if n & 1:
                ans *= x
            x *= x
            n = n >> 1
        if sign > 0:
            return ans
        else:
            return 1/ans


if __name__ == "__main__":
    print(Solution().myPow(2, 10))
    print(Solution().myPow(2.1, 3))
    print(Solution().myPow(2, -2))
