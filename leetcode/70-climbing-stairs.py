class Solution:
    # cache = {}
    # def climbStairs(self, n: int) -> int:
    #     if n <= 1:
    #         return 1
    #     if n in self.cache:
    #         return self.cache[n]
    #     last1 = self.climbStairs(n - 1)
    #     last2 = self.climbStairs(n - 2)
    #     res = last1 + last2
    #     self.cache[n] = res
    #     return res

    def climbStairs(self, n: int) -> int:
        return self.helper(1, 0, n)

    def helper(self, a, b, n):
        if n > 0:
            return self.helper(a+b, a, n-1)
        else:
            return a


if __name__ == "__main__":
    print(Solution().climbStairs(0))
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
