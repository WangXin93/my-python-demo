from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    def canJump3(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if m < i:
                return False
            m = max(i+n, m)
        return True

    def canJump2(self, nums: List[int]) -> bool:
        """ Use DFS, complexity O(V + E)
        """
        def dfs(i):
            if i >= len(nums):
                return False
            if i == len(nums) - 1:
                return True
            for child in range(i+1, i+nums[i]+1):
                if dfs(child):
                    return True
            return False
        return dfs(0)


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
