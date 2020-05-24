from typing import List


class Solution:
    # O(N)
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:1]
        decrease = dp.copy()
        for i, x in enumerate(nums[1:], 1):
            if i > k and decrease[0] == dp[i - k - 1]:
                decrease.pop(0)
            tmp = max(x, decrease[0] + x)
            dp.append(tmp)
            while decrease and decrease[-1] < tmp:
                decrease.pop()
            decrease.append(tmp)
        return max(dp)

    # This version is O(N M), too slow
    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     dp = []
    #     for i, e in enumerate(nums):
    #         dp.append(e)
    #         j = 1
    #         while j <= k and i-j >= 0:
    #             if dp[i-j] + e > dp[i]:
    #                 dp[i] = dp[i-j] + e
    #             j += 1
    #     return max(dp)


if __name__ == "__main__":
    print(Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2))  # 37
    print(Solution().constrainedSubsetSum([-1, -2, -3], 1))  # -1
    print(Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2))  # 23
